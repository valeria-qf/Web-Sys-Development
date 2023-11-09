from django.shortcuts import render
from .models import Aluno, Curso, Cidade

def Index(request):
    alunos = Aluno.objects.all()
    cidades = Cidade.objects.all()
    cursos = Curso.objects.all()

    context = {
        'alunos' : alunos,
        'cidades' : cidades,
        'cursos': cursos,
    }

    return render(request, 'core/index.html', context)
