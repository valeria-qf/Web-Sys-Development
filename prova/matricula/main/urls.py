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
from hospedagem.views import listar_hospedagens, index, criar_hospedagem, editar_hospedagem, excluir_hospedagem, detalhar_hospedagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('hospedagens/', listar_hospedagens, name = "listar_hospedagens"),
    path('hospedagens/criar', criar_hospedagem, name = "criar_hospedagem"),
    path('hospedagens/editar/<int:id>', editar_hospedagem, name = "editar_hospedagem"),
    path('hospedagens/excluir/<int:id>', excluir_hospedagem, name = "excluir_hospedagem"),
    path('hospedagens/detalhar/<int:id>', detalhar_hospedagem, name = "detalhar_hospedagem"),
]



