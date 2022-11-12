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