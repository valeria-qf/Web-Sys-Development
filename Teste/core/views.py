from django.shortcuts import render, redirect
from .models import Aluno, Curso, Cidade

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
        nome = request.POST.get('nome_aluno')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        curso_id = request.POST.get('curso')
        cidade_id = request.POST.get('cidade')

        curso = Curso.objects.get(pk=curso_id)
        cidade = Cidade.objects.get(pk=cidade_id)

        Aluno.objects.create(
            nome_aluno=nome,
            endereco=endereco,
            email=email,
            data_nascimento=data_nascimento,
            curso=curso,
            cidade=cidade
        )
        return redirect('core:index')
    
    cursos = Curso.objects.all()
    cidades = Cidade.objects.all()
    context = {
        'cursos': cursos,
        'cidades': cidades,
    }
    return render(request, 'core/create_aluno.html', context)

def update(request, id):
    if request.method == 'POST':
        nome = request.POST.get('nome_aluno')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        curso_id = request.POST.get('curso')
        cidade_id = request.POST.get('cidade')

        aluno = Aluno.objects.get(id = id)
        aluno.nome_aluno = nome
        aluno.endereco = endereco
        aluno.email = email
        aluno.data_nascimento = data_nascimento
        aluno.curso_id = curso_id
        aluno.cidade_id = cidade_id
        aluno.save()   

        return redirect('core:index')

    aluno = Aluno.objects.get(id = id)
    cursos = Curso.objects.all()
    cidades = Cidade.objects.all()

    context = {
        'aluno': aluno,
        'cursos': cursos,
        'cidades': cidades
    }
    return render(request, 'core/update.html', context)

def delete(request, id):
    if request.method == 'POST':
        aluno = Aluno.objects.get(id = id)
        aluno.delete()

    return redirect('core:index')

def detail(request, id):
    aluno = Aluno.objects.get(id = id)

    return render(request, 'core/detail.html', {'aluno':aluno})
