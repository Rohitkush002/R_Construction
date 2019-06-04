from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='Home'),
    path('sidebar', views.sidebar),
    path('header', views.header),
    path('ems', include('ems.urls')),
    path('sides', include('sides.urls')),
    path('vehicle', include('vehicle.urls')),
    path('', include('account.urls')),
]
