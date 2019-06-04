from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def sidebar(request):
    return render(request, "includes/sidebar.html")

def header(request):
    return render(request, "includes/header.html")
