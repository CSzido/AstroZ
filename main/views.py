from django.shortcuts import render
from .models import *
from django.contrib import messages
import json
from django.http import JsonResponse
# Create your views here.


def services(request):
    posts = Service.objects.all()
    context = {
        "products": posts
    }
    return render(request, "products.html", context)


def product(request, id):
    messages.success(request, "Don't forget your Email so that we can contact you!")
    post = Service.objects.get(id=id)
    context = {
        "product": post
    }
    return render(request, "product.html", context)


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    name = body['name']
    app_name = body['app_name']
    email = body['email']

    Order.objects.create(
        name=name,
        product_name=app_name,
        Email=email
        )
    return JsonResponse('Payment completed!', safe=False)