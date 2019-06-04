from django import forms
from .models import Driver, Fuel, Vehicle, ActiveVehicle


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'


class FuelForm(forms.ModelForm):
    class Meta:
        model = Fuel
        fields = '__all__'


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'



class ActiveVehicleForm(forms.ModelForm):
    class Meta:
        model = ActiveVehicle
        fields = '__all__'

