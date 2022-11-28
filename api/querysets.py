from django.db import models

class ActiveQuerySet(models.QuerySet):
    def delete(self):
        return self.update(active=False)
