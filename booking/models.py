from datetime import date
from typing import Set
import advertisement
from advertisement.models import Advertisement
from django.db import models
from challenge.utils import get_date_range_list, generate_random_code
from propriety.models import Propriety

BOOKING_CODE_MAX_LENGTH = 6
def generate_booking_code():
    return generate_random_code(BOOKING_CODE_MAX_LENGTH)

class BookingManager(models.Manager):

    def get_unavailable_dates_by_propriety(self, propriety: Propriety) -> Set[date]:
        bookings = self.model.objects.filter(
            advertisement__propriety=propriety
        )
        unavailable_dates = set()
        for booking in bookings:
            unavailable_dates.update(get_date_range_list(booking.check_in, booking.check_out))
        return unavailable_dates

class Booking(models.Model):
    objects = BookingManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=BOOKING_CODE_MAX_LENGTH, editable=False, default=generate_booking_code, unique=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    commentary = models.CharField(max_length=250)
    guests_count = models.IntegerField(default=1)

    def __str__(self):
        return str(self.pk)