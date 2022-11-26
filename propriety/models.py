from django.db import models

from challenge.utils import generate_random_code

PROPRIETY_CODE_MAX_LENGTH = 6
def generate_propriety_code():
    return generate_random_code(PROPRIETY_CODE_MAX_LENGTH)

class Propriety(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False, editable=False)
    activation_date = models.DateTimeField(blank=False, null=False)
    code = models.CharField(max_length=PROPRIETY_CODE_MAX_LENGTH, blank=False, null=False, editable=False, default=generate_propriety_code, unique=True)
    guests_limit = models.IntegerField(null=False, blank=False)
    bathroom_count = models.IntegerField(null=False, blank=False)
    pet_frendly = models.BooleanField(null=False, blank=False)
    cleaner_fee = models.DecimalField(decimal_places=2, max_digits=9, null=False, blank=False)

    def __str__(self):
        return str(self.pk)