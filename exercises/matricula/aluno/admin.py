from django.contrib import admin
from .models import Aluno, Cidade, Curso, Coordenador

admin.site.register(Aluno)
admin.site.register(Cidade)
admin.site.register(Curso)
admin.site.register(Coordenador)


