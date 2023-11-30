from django.contrib import admin
from parkingapp.models import Contact,ParkingArea,UserReservation

# Register your models here.
admin.site.register(Contact)
admin.site.register(ParkingArea)
admin.site.register(UserReservation)