from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.email