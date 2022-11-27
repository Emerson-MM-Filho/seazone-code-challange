from django.db import models
from propriety.models import Propriety


class Advertisement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    propriety = models.ForeignKey(Propriety, on_delete=models.CASCADE)
    platform = models.CharField(max_length=250, null=False, blank=False)
    platform_fee = models.DecimalField(decimal_places=2, max_digits=9, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.pk} - {self.platform} - {self.propriety.code}"