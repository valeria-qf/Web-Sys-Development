from django.shortcuts import render, redirect
from .models import Aluno, Curso, Cidade
from .forms import AlunoForm

def index(request):
    alunos = Aluno.objects.all()
    cidades = Cidade.objects.all()
    cursos = Curso.objects.all()
    
    context = {
        'alunos': alunos,
        'cidades': cidades,
        'cursos': cursos,
    }

    return render(request, 'core/index.html', context)

def create_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('core:index')  
    
    else:
        form = AlunoForm()
        cursos = Curso.objects.all()
        cidades = Cidade.objects.all()

        context = {
            'form': form,
            'cursos': cursos,
            'cidades': cidades
        }

    return render(request, 'core/create_aluno.html', context)

def update(request, id):

    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()

            return redirect('core:index')

    else:
        cursos = Curso.objects.all()
        cidades = Cidade.objects.all()

        context = {
            'aluno': aluno,
            'cursos': cursos,
            'cidades': cidades
        }

        return render(request, 'core/update.html', context)

def delete(request, id):
    aluno = Aluno.objects.get(id = id)
    aluno.delete()

    return redirect('core:index')

def detail(request, id):
    aluno = Aluno.objects.get(id = id)

    return render(request, 'core/detail.html', {'aluno':aluno})
