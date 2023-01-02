from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


@api_view(['POST'])
def payment(request):
    service_id = request.POST.get('service')
    account_number = request.POST.get('number')
    amount = request.POST.get('amount')
    phone = request.POST.get('phone')
    service = Service.objects.get(id=service_id)
    new_payment = Payment.objects.create(
        service=service,
        account_number=account_number,
        amount=amount
    )
    if request.user.is_authenticated():
        new_payment.user = request.user
        new_payment.phonec = request.user.phone
        new_payment.save()
    else:
        new_payment.phone = phone
        new_payment.save()
    service.balance += (amount - ())
