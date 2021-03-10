from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def data(request):
    return render(request, 'data.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dog/index.html', {'dogs':dogs})



