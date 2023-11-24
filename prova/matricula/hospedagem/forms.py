from django.forms import ModelForm
from django import forms
from .models import Hospedagem

class HospedagemForm(ModelForm):

    class Meta:
        model = Hospedagem
        fields = '__all__'
        widgets = {
            'cliente' : forms.Select(attrs={'class': 'form-control' }),
            'data_entrada' : forms.DateInput(attrs={'class': 'form-control' }),
            'data_saida' : forms.DateInput(attrs={'class': 'form-control' }),
            'valor': forms.NumberInput(attrs={'class': 'form-control' }),
            'quarto': forms.Select(attrs={'class': 'form-control' })
        }
