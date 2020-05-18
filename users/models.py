from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=50)

    def __str__(self):
        return self.email
