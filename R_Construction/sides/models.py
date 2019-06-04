from django.db import models


class SideIncharge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Side(models.Model):
    sideName = models.CharField(max_length=100)
    sideAdd = models.TextField(blank=True, null=True)
    sideIncharge = models.ForeignKey(SideIncharge, on_delete=models.CASCADE)
    vehicles = models.CharField(max_length=200)
    activeVehicle = models.CharField(max_length=200)
    employee = models.CharField(max_length=100)

    def __str__(self):
        return self.sideName


class Work(models.Model):
    SideName = models.ForeignKey(Side, on_delete=models.CASCADE)

