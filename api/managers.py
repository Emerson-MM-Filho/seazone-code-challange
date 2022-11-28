from django.db import models
from.querysets import ActiveQuerySet

class ActiveManager(models.Manager):

    def active(self):
        return self.model.objects.filter(active=True)

    def get_queryset(self):
        return ActiveQuerySet(model=self.model, using=self._db, hints=self._hints)
