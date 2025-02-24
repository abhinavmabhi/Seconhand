from django.contrib import admin
from .models import Category, Brand, VehicleModel, Vehicle,Car_or_Bike

# Register your models here.
admin.site.register(Car_or_Bike)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(VehicleModel)
admin.site.register(Vehicle)

