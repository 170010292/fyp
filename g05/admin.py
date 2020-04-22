from django.contrib import admin
from .models import Airlinecompany, Airplane, Airplaneticket, Attraction, Attractioncompany, Attractionticket
# Register your models here.

@admin.register(Airlinecompany)
class Airline(admin.ModelAdmin):
    list_display = ('airlinecompanyname', 'airlinecompanyno', 'airlinecompanyaddress')

admin.site.register(Airplane)
admin.site.register(Airplaneticket)
admin.site.register(Attraction)
admin.site.register(Attractioncompany)
admin.site.register(Attractionticket)