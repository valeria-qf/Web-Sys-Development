from django.shortcuts import render, redirect, get_object_or_404
from aluno.models import Curso
from .forms import CursoForm
# Create your views here.

def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/curso.html', {'cursos' : cursos})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id = id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance = curso)
        if form.is_valid():
            form.save()
            return redirect('ver_cursos')
        else:
            print(form.errors)
    else:
        form = CursoForm(instance = curso)
        return render(request, 'curso/form_curso.html', {'form' : form})

def criar_curso(request): 
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_cursos')
        else:
            print(form.errors)
    else:
        form = CursoForm()
    return render(request, 'curso/form_curso.html', {'form': form})

def excluir_curso(request, id):
    curso = get_object_or_404(Curso, id = id)
    curso.delete()
    return redirect('ver_cursos') 




