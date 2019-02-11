from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'rincon/index.html')

def menu(request):
    return render(request, 'rincon/menu.html')

def location(request):
    return render(request, 'rincon/location.html')

def order(request):
    return render(request, 'rincon/order.html')

def about(request):
    return render(request, 'rincon/about.html')
