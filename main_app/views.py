from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog,Cat
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def data(request):
    return render(request, 'data.html')

# Views for Dogs
def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dog/index.html', {'dogs':dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dog/detail.html', {'dog': dog})

# Views for Cats
def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cat/index.html', {'cats':cats})

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cat/detail.html', {'cat': cat})




