"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aluno import views as views_aluno
from curso import views as views_curso
from cidade import views as views_cidade

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_aluno.index, name = 'index'),
    path('listar-alunos', views_aluno.ver_alunos, name='ver_alunos'),
    path('criar-aluno/', views_aluno.criar_aluno, name= 'criar_aluno'),
    path('editar-aluno/<int:id>/', views_aluno.editar_aluno, name = 'editar_aluno'),
    path('excluir-aluno/<int:id>/', views_aluno.excluir_aluno, name = 'excluir_aluno'),

    path('listar-cursos', views_curso.ver_cursos, name = 'ver_cursos' ),
    path('criar-curso', views_curso.criar_curso, name = 'criar_curso'),
    path('editar-curso/<int:id>', views_curso.editar_curso, name = 'editar_curso'),
    path('excluir-curso/<int:id>', views_curso.excluir_curso, name = 'excluir_curso'),

    path('listar-cidades/', views_cidade.ver_cidades, name = 'ver_cidades'),
    path('criar-cidade/', views_cidade.criar_cidade, name = 'criar_cidade'),
    path('editar-cidade/<int:id>', views_cidade.editar_cidade, name = 'editar_cidade'),
    path('excluir-cidade/<int:id>', views_cidade.excluir_cidade, name = 'excluir_cidade'),
]

