from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from .forms import UUIDUserForm

class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'cadastrouser.html'
    success_url = reverse_lazy('sisevento:login')
    form_class = UUIDUserForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(UserCreate, self).form_valid(form)

class Home (TemplateView):
	template_name = 'home.html'