from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from .forms import UUIDUserForm, Atividade, Evento
class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'cadastrouser.html'
    success_url = reverse_lazy('sisevento:login')
    form_class = UUIDUserForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(UserCreateView, self).form_valid(form)

class Home (TemplateView):
	template_name = 'home.html'

class Atividade(CreateView):
    model = models.Atividade
    template_name = 'atividade.html'
    success_url = reverse_lazy('sisevento:home')
    form_class = Atividade
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.criador = self.request.user 
        obj.save()
        return super(Atividade, self).form_valid(form)

class Veratividade(ListView):
    model = models.Atividade
    template_name = 'veratividade.html'

class Eventos(CreateView):
    model = models.Eventos
    template_name = 'eventos.html'
    success_url = reverse_lazy('sisevento:home')
    form_class = Evento
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.criador = self.request.user 
        obj.save()
        return super(Eventos, self).form_valid(form)

class ListEvento (ListView):
    model = models.Eventos
    template_name = 'listareventos.html'

