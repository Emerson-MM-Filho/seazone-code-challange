from datetime import date
from rest_framework import serializers

from advertisement.models import Advertisement
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def _validate_check_out_date(self) -> None:
        data = self._kwargs['data']
        check_in_date = date.fromisoformat(data['check_in'])
        check_out_date = date.fromisoformat(data['check_out'])

        if check_in_date > check_out_date:
            raise serializers.ValidationError('The check-out date must be later than the check-in date')

    def _validate_guests_count(self) -> None:
        guests_count = int(self._kwargs['data']['guests_count'])
        advertisement_id = self._kwargs['data']['advertisement']
        advertisement = Advertisement.objects.get(id=advertisement_id)

        if guests_count > advertisement.propriety.guests_limit:
            raise serializers.ValidationError('The check-out date must be later than the check-in date')

    def is_valid(self, *args, **kwargs):
        self._validate_check_out_date()
        self._validate_guests_count()

        super().is_valid(*args, **kwargs)
