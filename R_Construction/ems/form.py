from django import forms
from .models import Designation, Employee


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
