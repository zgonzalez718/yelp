from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'rincon/index.html')

def menu(request):
    return render(request, 'rincon/menu.html')
