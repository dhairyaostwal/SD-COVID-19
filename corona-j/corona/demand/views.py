from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'demand/dashboard.html')

def about(request):
    return render(request, 'demand/about.html')

def services(request):
    return render(request, 'demand/services.html')
    
