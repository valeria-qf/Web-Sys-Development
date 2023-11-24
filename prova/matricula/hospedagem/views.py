from django.shortcuts import render, redirect, get_object_or_404
from .models import Hospedagem, Cliente, Consumo, Quarto 
from .forms import HospedagemForm

def index(request):
    # total_hospedagens = Hospedagem.objects.count()
    # # total_cidades = Cidade.objects.count()
    # # total_curso = Curso.objects.count()
    # context = {
    #     'total_alunos' : total_alunos,
    #     'total_cidades' : total_cidades,
    #     'total_cursos' : total_curso
    
    return render(request, "hospedagem/index.html")


def listar_hospedagens(request):
    hospedagens = Hospedagem.objects.all()
    return render(request, 'hospedagem/hospedagem.html', {'hospedagens' : hospedagens})

def criar_hospedagem(request):
    if request.method == 'POST':
        form = HospedagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_hospedagens')
    else:
        form = HospedagemForm()
        return render(request, 'hospedagem/form_hospedagem.html', {'form' : form})
    
def editar_hospedagem(request, id):
    hospedagem = get_object_or_404(Hospedagem, id = id)
    if request.method == 'POST':
        form = HospedagemForm(request.POST, instance= hospedagem)
        if form.is_valid():
            form.save()
            return redirect('listar_hospedagens')
    else:
        form = HospedagemForm(instance= hospedagem)
        return render(request, 'hospedagem/form_hospedagem.html', {'form' : form})

def excluir_hospedagem(request, id):
    hospedagem = get_object_or_404(Hospedagem, id = id)
    hospedagem.delete()
    return redirect('listar_hospedagens')

def detalhar_hospedagem(request, id):
    hospedagem = get_object_or_404(Hospedagem, id = id)
    return render(request, 'hospedagem/detalhar.html', {'hospedagem' : hospedagem})

