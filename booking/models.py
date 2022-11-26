from os import urandom
from advertisement.models import Advertisement
from django.db import models


def generate_random_code(cls):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(chars[c % len(chars)] for c in urandom(6))

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    code = models.UUIDField(blank=False, null=False, editable=False, default=generate_random_code, unique=True)
    advertisement_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE, null=False, blank=False)
    check_in = models.DateField(null=False, blank=False)
    check_out = models.DateField(null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=9, null=False, blank=False)
    commentary = models.CharField(max_length=250, null=False, blank=False)
    guests_count = models.IntegerField(null=False, blank=False)