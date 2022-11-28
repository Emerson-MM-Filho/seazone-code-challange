from django.db import models
from propriety.models import Propriety
from api.managers import ActiveManager

class Advertisement(models.Model):
    objects = ActiveManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    propriety = models.ForeignKey(Propriety, on_delete=models.CASCADE)
    platform = models.CharField(max_length=250)
    platform_fee = models.DecimalField(decimal_places=2, max_digits=9)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.pk} - {self.platform} - {self.propriety.code}"

    def delete(self):
        self.active = False
        self.save()
