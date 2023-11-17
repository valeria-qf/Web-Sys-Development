from django.shortcuts import render, redirect, get_object_or_404
from .forms import CidadeForm
from aluno.models import Cidade

# Create your views here.

def ver_cidades(request):
    cidades = Cidade.objects.all()
    return render(request, 'cidade/cidade.html', {'cidades' : cidades})

def criar_cidade(request):
    if request.method == 'POST':
        form_cidade = CidadeForm(request.POST)
        if form_cidade.is_valid():
            form_cidade.save()
            return redirect('ver_cidades')
    else:
        form_cidade = CidadeForm()
        return render(request, 'cidade/form_cidade.html', {'form_cidade': form_cidade})

def editar_cidade(request, id):
    cidade = get_object_or_404(Cidade, id = id)
    if request.method == 'POST':
        form_cidade = CidadeForm(request.POST, instance= cidade)
        if form_cidade.is_valid():
            form_cidade.save()
            return redirect('ver_cidades')
    
    else:
        form_cidade = CidadeForm(instance= cidade)
        return render(request, 'cidade/form_cidade.html', {'form_cidade':form_cidade})
    
def excluir_cidade(request, id):
    cidade = get_object_or_404(Cidade, id = id)
    cidade.delete()
    return redirect('ver_cidades')

