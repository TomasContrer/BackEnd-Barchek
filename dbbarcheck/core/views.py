from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Alcohol
from .forms import AlcoholForm  # lo crearás en el paso siguiente

# Listar todos los registros
def alcohol_list(request):
    alcoholes = Alcohol.objects.all()
    return render(request, 'core/alcohol_list.html', {'alcoholes': alcoholes})

# Crear un nuevo registro
def alcohol_create(request):
    if request.method == 'POST':
        form = AlcoholForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alcohol_list')
    else:
        form = AlcoholForm()
    return render(request, 'core/alcohol_form.html', {'form': form})

# Editar un registro existente
def alcohol_update(request, pk):
    alcohol = get_object_or_404(Alcohol, pk=pk)
    if request.method == 'POST':
        form = AlcoholForm(request.POST, instance=alcohol)
        if form.is_valid():
            form.save()
            return redirect('alcohol_list')
    else:
        form = AlcoholForm(instance=alcohol)
    return render(request, 'core/alcohol_form.html', {'form': form})

# Eliminar un registro
def alcohol_delete(request, pk):
    alcohol = get_object_or_404(Alcohol, pk=pk)
    if request.method == 'POST':
        alcohol.delete()
        return redirect('alcohol_list')
    return render(request, 'core/alcohol_confirm_delete.html', {'alcohol': alcohol})
