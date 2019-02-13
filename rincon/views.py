from django.shortcuts import render
from .models import Food

# Create your views here.

def index(request):
    return render(request, 'rincon/index.html')

def menu(request):
    food = Food.objects
    return render(request, 'rincon/menu.html',{'foods':food})

def location(request):
    return render(request, 'rincon/location.html')

def order(request):
    return render(request, 'rincon/order.html')

def about(request):
    return render(request, 'rincon/about.html')
