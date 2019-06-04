from django.shortcuts import render, get_object_or_404, redirect
from .forms import VehicleForm, DriverForm, ActiveVehicleForm
from django.contrib import messages
from .models import Vehicle, ActiveVehicle


def vehicle(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicleList')

    data = {
        'form': form
    }
    return render(request, 'vehicle_page/vehicle.html', data)


def vehiclelist(request):
    vl = Vehicle.objects.all()
    data = {
        'vl': vl
    }
    return render(request, 'vehicle_page/vehicleList.html', data)


def activevehicle(request):
    form = ActiveVehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('activeList')

    data = {
        'form': form
    }
    return render(request, 'vehicle_page/activeVehicle.html', data)


def activelist(request):
    al = ActiveVehicle.objects.all()
    data = {
        'al': al
    }
    return render(request, 'vehicle_page/activeList.html', data)


def delete(request, id):
    obj = Vehicle.objects.get(id=id)

    obj.delete()
    return redirect('vehicleList')
    messages.success(request, 'Records Deleted Successfully....')

    return render(request, 'vehicleList.html', data)


def update(request, id):
    sd = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(request.POST or None, instance=sd)
    if form.is_valid():
        sd.save()
        return redirect('vehicleList')
    messages.success(request, 'Records Updated Successfully....')
    data = {
        'form': form,
        'sd': sd,
    }
    return render(request, 'vehicle_page/update.html', data)


# adding driver name

def driver(request):
    form = DriverForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('vehicle')
    data = {
        'form': form
    }
    return render(request, 'vehicle_page/driver.html', data)
