from django import forms
from aluno.models import Cidade

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'
        widgets = {
            'nome_cidade': forms.TextInput(attrs={'class': 'form-control' }),
            'sigla_estado': forms.TextInput(attrs={'class': 'form-control' }),
         }
