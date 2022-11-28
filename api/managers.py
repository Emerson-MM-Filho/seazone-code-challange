from django.db import models

class ActiveManager(models.Manager):

    def active(self):
        """Returns all active instances of the model"""
        return self.model.objects.filter(active=True)
