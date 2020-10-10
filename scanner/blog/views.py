from django.shortcuts import render
from .models import Devices
#from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    context = {
        "Devices": Devices.objects.all()
    }
    return render(request, 'blog/login.html', context)

def dashboard(request):
    context = {
        "Devices": Devices.objects.all()
    }
    return render(request, 'blog/index.html', context)

def login(request):
    return render(request, 'blog/login.html')

def tables(request):
    context = {
            "Devices": Devices.objects.all()
        }
    return render(request, 'blog/tables.html', context)
