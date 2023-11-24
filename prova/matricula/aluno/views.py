# from django.shortcuts import render,get_object_or_404,redirect
# from .models import Aluno,Curso,Cidade
# from .forms import AlunoForm

# def aluno_editar(request,id):
#     aluno = get_object_or_404(Aluno,id=id)
   
#     if request.method == 'POST':
#         form = AlunoForm(request.POST,instance=aluno)

#         if form.is_valid():
#             form.save()
#             return redirect('aluno_listar')
#     else:
#         form = AlunoForm(instance=aluno)

#     return render(request,'aluno/form.html',{'form':form})


# def aluno_remover(request, id):
#     aluno = get_object_or_404(Aluno, id=id)
#     aluno.delete()
#     return redirect('aluno_listar') # procure um url com o nome 'lista_aluno'


# def aluno_criar(request):
#     if request.method == 'POST':
#         form = AlunoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = AlunoForm()
#     else:
#         form = AlunoForm()

#     return render(request, "aluno/form.html", {'form': form})


# def aluno_listar(request):
#     alunos = Aluno.objects.all()
#     context ={
#         'alunos':alunos
#     }
#     return render(request, "aluno/alunos.html",context)

