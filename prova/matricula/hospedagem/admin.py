from django.contrib import admin
from .models import Hospedagem, Cliente, Consumo, Quarto

# Register your models here.

admin.site.register(Hospedagem)
admin.site.register(Cliente)
admin.site.register(Consumo)
admin.site.register(Quarto)
