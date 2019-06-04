from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import SignUp
from django.contrib.auth import logout

def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
    data = {
        'form': form
    }
    return render(request, 'account/signup.html', data)

def login(request):
        if request.session.get('username', None):
            return redirect('login')

        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')

                user_auth = SignUp.objects.filter(email=email, password=password)
                if user_auth.exists():
                    print("Session:", type(request.session))
                    request.session['email'] = email
                    return redirect('Home')

        data = {
            "form": form
        }
        return render(request, 'account/login.html', data)


def logout(request):
        logout(request)

        return redirect('login')
