from django.db import models
from django.conf import settings
# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
