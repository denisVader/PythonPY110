from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from random import random
from django.http import HttpResponse

def datetime_view(request):
    if request.method == "GET":
        data = datetime.now()  # Написать, что будет возвращаться из данного представления
        return HttpResponse(data)# Вернуть объект HttpResponse с необходимыми данными

# Create your views here.
