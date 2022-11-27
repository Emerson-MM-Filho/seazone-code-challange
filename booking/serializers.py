from datetime import date
from rest_framework import serializers

from challenge.utils import get_date_range_list

from .models import Booking
from api.error_code import ErrorCode
from advertisement.models import Advertisement


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def _validate_check_out_date(self, check_in: date, check_out: date) -> None:
        if check_in > check_out:
            raise serializers.ValidationError(
                {"check_out": f"The check-out ({check_out}) date must be later than the check-in ({check_in}) date"},
                code=ErrorCode.INVALID_FIELD.value
            )

    def _validate_guests_count(self, guests_count: int, advertisement: Advertisement) -> None:
        if guests_count > advertisement.propriety.guests_limit:
            raise serializers.ValidationError(
                {"guests_count": f"The maximum number of guests is: {advertisement.propriety.guests_limit}"},
                code=ErrorCode.INVALID_FIELD.value
            )

    def _validate_available_date(self, check_in: date, check_out: date, advertisement: Advertisement) -> None:
        indicated_dates_set = get_date_range_list(check_in, check_out)
        unavailable_dates_set = Booking.objects.get_unavailable_dates_by_propriety(advertisement.propriety)

        for date in indicated_dates_set:
            if date in unavailable_dates_set:
                raise serializers.ValidationError(
                    {"check_in/check_out": f"Property {advertisement.propriety} is already booked for the indicated dates"},
                    code=ErrorCode.INVALID_BOOKING_SCHEDULING.value
                )

    def validate(self, *args, **kwargs):
        exc_dict = dict()

        try:
            self._validate_check_out_date(args[0]["check_in"], args[0]["check_out"])
        except serializers.ValidationError as exc:
            exc_dict.update(**exc.get_full_details())

        try:
            self._validate_guests_count(args[0]["guests_count"], args[0]["advertisement"])
        except serializers.ValidationError as exc:
            exc_dict.update(**exc.get_full_details())

        try:
            self._validate_available_date(args[0]["check_in"], args[0]["check_out"], args[0]["advertisement"])
        except serializers.ValidationError as exc:
            exc_dict.update(**exc.get_full_details())

        if exc_dict:
            raise serializers.ValidationError(exc_dict)

        return super().validate(*args, **kwargs)
