from datetime import date
from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def is_valid(self, *args, **kwargs):
        data = self._kwargs['data']

        check_in_date = date.fromisoformat(data['check_in'])
        check_out_date = date.fromisoformat(data['check_out'])

        if check_in_date > check_out_date:
            raise serializers.ValidationError('The check-out date must be later than the check-in date')

        super().is_valid(*args, **kwargs)