from django.db import models


class Designation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    Designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
