from django.urls import path
from . import views as vehicle_view

urlpatterns = [
    path('vehicle/', vehicle_view.vehicle, name='vehicle'),
    path('vehiclelist/', vehicle_view.vehiclelist, name='vehicleList'),
    path('activevehicle/', vehicle_view.activevehicle, name='activeVehicle'),
    path('activelist/', vehicle_view.activelist, name='activeList'),
    path('driver/', vehicle_view.driver, name='driver'),
    path('delete/<int:id>', vehicle_view.delete, name='delete_vehicle'),
    path('update/<int:id>', vehicle_view.update, name='update_vehicle'),

]
