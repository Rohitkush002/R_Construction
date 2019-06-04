from django.contrib import admin

from .models import Driver, Fuel, Vehicle,ActiveVehicle

admin.site.register(Driver)
admin.site.register(Fuel)
admin.site.register(Vehicle)
admin.site.register(ActiveVehicle)
