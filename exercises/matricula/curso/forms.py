from aluno.models import Curso
from django import forms

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'nome_curso': forms.TextInput(attrs={'class': 'form-control' }),
            'coordenador_curso': forms.Select(attrs={'class': 'form-control' }),
        }