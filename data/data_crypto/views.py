
from django.shortcuts import render, HttpResponse
from .models import Data_crypto

def data_list(request):
    data_crypto = Data_crypto.objects.all().order_by('date')
    return render(request, "data_crypto/data_list.html", {"data_crypto" : data_crypto})

def data_detail(request, slug):
    data_crypto = Data_crypto.objects.get(slug=slug)
    return render(request, "data_crypto/data_detail.html", {"data_crypto": data_crypto})