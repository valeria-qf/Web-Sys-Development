from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_aluno/', views.create_aluno, name='create_aluno'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('detail/<int:id>', views.detail, name='detail'),
]
