from django.db import models
from account.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class TypeService(models.Model):
    name = models.CharField(max_length=255)
    percent = models.IntegerField(default=0, validators=[MaxValueValidator(10)])
    cash_back = models.IntegerField(default=0, validators=[MaxValueValidator(10)])


class Service(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_service = models.ForeignKey(TypeService, on_delete=models.SET_NULL)
    balance = models.BigIntegerField()
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255)
    amount = models.IntegerField()
    phone = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

