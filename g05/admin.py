from django.contrib import admin
from .models import Airlinecompany, Airplane, Airplaneticket, Attraction, Attractioncompany, Attractionticket
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

admin.site.register(Attraction)
admin.site.register(Attractioncompany)
admin.site.register(Attractionticket)