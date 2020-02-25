from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def travel(request):
    return render(request, 'travel.html')

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