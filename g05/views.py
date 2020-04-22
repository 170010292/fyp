from django.shortcuts import render
from django.http import HttpResponse
from g05 .models import AuthUser , Airlinecompany
from django.views import generic

# Create your views here.

def index(request):
    return render(request, 'index.html')

def travel(request):
    Travels = Airlinecompany.objects.all()
    return render(request, 'travel.html',locals())

def movie(request):
    return render(request, 'movie.html')

def food(request):
    return render(request, 'food.html')

def show(request):
    return render(request, 'show.html')

def tour(request):
    return render(request, 'tour.html')

def themepark(request):
    return render(request, 'themepark.html')