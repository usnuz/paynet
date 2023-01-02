from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.IntegerField()
    status = models.IntegerField(default=0, choices=(
        (0, 'Customer'),
        (1, 'Company'),
        (2, 'Admin'),
    ))
    balance = models.IntegerField(default=0)
    address = models.CharField(max_length=255)

    class Mete(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



