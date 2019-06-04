from django.db import models
from sides.models import Side


class Driver(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Fuel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    VehicleNo = models.CharField(max_length=50)
    driverName = models.ForeignKey(Driver, on_delete=models.CASCADE)
    fuelType = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    allotedSideName = models.ForeignKey(Side, on_delete=models.CASCADE)

    def __str__(self):
        return self.VehicleNo


class ActiveVehicle(models.Model):
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
