from django.shortcuts import render
from django.http import HttpResponseRedirect
from g05 .models import Airplaneticket,Movieticket
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'index.html',locals())

def travel(request):
    Airplanes = Airplaneticket.objects.all()
    return render(request, 'travel.html',locals())

def movie(request):
    moviess = Movieticket.objects.all()
    return render(request, 'movie.html',locals())

def food(request):
    return render(request, 'food.html')

def show(request):
    return render(request, 'show.html',locals())

def tour(request):
    return render(request, 'tour.html',locals())

def themepark(request):
    return render(request, 'themepark.html',locals())

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())