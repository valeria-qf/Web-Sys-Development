from .models import Hospedagem
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView

from django.urls import reverse_lazy
from .forms import HospedagemForm

class Index(TemplateView):
    template_name = 'hospedagem/index.html'
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['total_alunos'] = Aluno.objects.count()
        # context['total_cidades'] = Cidade.objects.count()
        # context['total_cursos'] = Curso.objects.count()
        # return context

class ListarHospedagens(ListView):
    model = Hospedagem
    template_name = 'hospedagem/hospedagem.html'
    context_object_name = 'hospedagens'
    
class CriarHospedagem(CreateView):
    template_name = 'hospedagem/form_hospedagem.html'
    form_class = HospedagemForm
    success_url = reverse_lazy('listar_hospedagens')
   
class EditarHospedagem(UpdateView):
    model = Hospedagem
    template_name = 'hospedagem/form_hospedagem.html'
    form_class = HospedagemForm
    pk_url_kwarg = 'id' # Nome da variavel na URL

    def get_success_url(self):
        return reverse_lazy('listar_hospedagens')

class ExcluirHospedagem(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy('listar_hospedagens')
    pk_url_kwarg = 'id'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class DetalharHospedagem(DetailView):
    model = Hospedagem
    template_name = 'hospedagem/detalhar.html'
    pk_url_kwarg = 'id'

