from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=15, blank=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
