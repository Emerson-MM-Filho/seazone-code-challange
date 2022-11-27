from django.db import models


class Propriety(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    activation_date = models.DateTimeField()
    code = models.CharField(max_length=250, unique=True)
    guests_limit = models.IntegerField(default=1)
    bathroom_count = models.IntegerField(default=1)
    pet_frendly = models.BooleanField(default=False)
    cleaner_fee = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.code