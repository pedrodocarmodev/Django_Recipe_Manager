from django.db import models

# Create your models here.
class StorageItem(models.Model):
    name = models.CharField(max_length=127)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name