from django import forms
from .models import SignUp


class SignupForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'


class LoginForm(forms.Form):
    email = forms.CharField(max_length=40,
                            label="Email",
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Email',
                                    'email': 'email'
                                }))

    password = forms.CharField(max_length=40,
                               label="Password",

                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Enter Password',
                                       'name':'psw'
                                   }))

