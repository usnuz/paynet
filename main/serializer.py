from rest_framework import serializers
from .models import *


class PaymentSerializer(serializers.ModelSerializer):
    model = Payment
    fields = '__all__'
