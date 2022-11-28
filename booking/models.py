from advertisement.models import Advertisement
from django.db import models
from challenge.utils import generate_random_code

from .managers import BookingManager

BOOKING_CODE_MAX_LENGTH = 6
def generate_booking_code():
    return generate_random_code(BOOKING_CODE_MAX_LENGTH)

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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            return
        super().save(*args, **kwargs)
