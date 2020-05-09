from django.contrib import admin
from .models import Airlinecompany, Airplane, Airplaneticket, Movie, Moviecompany, Movietheater,Movieticket
# Register your models here.

@admin.register(Airlinecompany)
class Airline(admin.ModelAdmin):
    list_display = ('airlinecompanyname', 'airlinecompanyno', 'airlinecompanyaddress')

@admin.register(Airplane)
class Airplane(admin.ModelAdmin):
    list_display = ('airplaneid', 'airlinecompanyid', 'checkinport', 'meal')

@admin.register(Airplaneticket)
class Airplaneticket(admin.ModelAdmin):
    list_display = ('airplaneticketid', 'airplaneid')

@admin.register(Movie)
class Movie(admin.ModelAdmin):
    list_display = ('movieid', 'moviename', 'moviecompanyid')

@admin.register(Moviecompany)
class Moviecompany(admin.ModelAdmin):
    list_display = ('moviecompanyid', 'moviecompanyname', 'moviecompanyno','moviecompanyaddress','moviecompanyemail')

@admin.register(Movietheater)
class Movietheater(admin.ModelAdmin):
    list_display = ('theaterid', 'theatername', 'theateraddress','moviecompanyid')

@admin.register(Movieticket)
class Movieticket(admin.ModelAdmin):
    list_display = ('movieticketid', 'moviedate', 'moviestarttime', 'movieendtime', 'movieroom', 'movieseat', 'price', 'movieid', 'theaterid')