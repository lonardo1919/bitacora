from django.shortcuts import render, redirect
from app_1.models import Habitat
from app_1.forms import formHabitat

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def insert_habitat_view(request):
    form = formHabitat()
    if request.method == 'POST':
        form = formHabitat(request.POST)
        if form.is_valid():
            form.save()
        return home_view(request)
    data = {'form':form}
    return render (request,'habitat_agregar.html', data)

def list_habitat_view(request):
    habitat = Habitat.objects.all()
    data = {'habitat':habitat}
    return render(request, 'habitat_listado.html', data)

def delete_habitat_view(request, id):
    habitat = Habitat.objects.get(id=id)
    data = {'habitat':habitat}
    return redirect('view00')

def update_habitat_view(request, id):
    habitat = Habitat.objects.get(id=id)
    form = formHabitat(instance=id)
    if request.method == 'POST':
        form = formHabitat(request.POST,instance=habitat)
        if form.is_valid():
            form.save()
        return home_view(request)
    data = {'form':form}
    return render(request,'habitat_agregar.html', data)