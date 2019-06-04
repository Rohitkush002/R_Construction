from django import forms
from .models import SideIncharge, Side, Work


class SideInchargeForm(forms.ModelForm):
    class Meta:
        model = SideIncharge
        fields = '__all__'


class SideForm(forms.ModelForm):
    class Meta:
        model = Side
        fields = '__all__'


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
