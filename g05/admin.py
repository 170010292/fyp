from django.contrib import admin
from .models import Airlinecompany, Airplane, Airplaneticket, Attraction, Attractioncompany, Attractionticket
# Register your models here.

admin.site.register(Airlinecompany)
admin.site.register(Airplane)
admin.site.register(Airplaneticket)
admin.site.register(Attraction)
admin.site.register(Attractioncompany)
admin.site.register(Attractionticket)