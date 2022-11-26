from django.db import models


class Propriety(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False, editable=False)
    activation_date = models.DateTimeField(blank=False, null=False)
    code = models.CharField(max_length=250, null=False, blank=False)
    guests_limit = models.IntegerField(null=False, blank=False)
    bathroom_count = models.IntegerField(null=False, blank=False)
    pet_frendly = models.BooleanField(null=False, blank=False)
    cleaner_fee = models.DecimalField(decimal_places=2, max_digits=9, null=False, blank=False)