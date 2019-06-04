from django.urls import path
from . import views as account_view

urlpatterns = [
    path('signup/', account_view.signup, name='signup'),
    path('', account_view.login, name='login'),
    path('logout/', account_view.logout, name='logout'),

]
