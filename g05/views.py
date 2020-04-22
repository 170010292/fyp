from django.shortcuts import render
from django.http import HttpResponse
from g05 .models import AuthUser

# Create your views here.

def index(request):
    return render(request, 'index.html')

def travel(request):
    num_AuthUser = AuthUser.objects.all().count()
    context = {
        'num_AuthUser': num_AuthUser,
    }
    return render(request, 'travel.html', context=context)

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