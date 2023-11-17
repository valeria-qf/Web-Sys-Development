from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno,Curso,Cidade
from .forms import AlunoForm

def ver_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/alunos.html', {'alunos': alunos})

def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ver_alunos')
    else:
        form = AlunoForm()
        return render(request, 'aluno/form.html', {'form': form})
    
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id = id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance= aluno)
        if form.is_valid():
            form.save()
        return redirect('ver_alunos')
    
    else:
        form = AlunoForm(instance = aluno)
        return render(request, 'aluno/form.html', {'form': form})
    
def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id = id)
    aluno.delete()
    return redirect(ver_alunos)

def index(request):
    total_alunos = Aluno.objects.count()
    total_cidades = Cidade.objects.count()
    total_curso = Curso.objects.count()
    context = {
        'total_alunos' : total_alunos,
        'total_cidades' : total_cidades,
        'total_cursos' : total_curso
    }
    return render(request, "aluno/index.html", context)




