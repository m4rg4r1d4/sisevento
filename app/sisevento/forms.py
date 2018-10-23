#coding:utf-8

from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import UUIDUser, Atividade, Eventos

# User: create
# - - - - - - - - - - - - - - - - - - -
class UUIDUserForm(forms.ModelForm):
    class Meta:
        model = UUIDUser
        fields = ('username', 'password', 'email', 'cpf', 'telefone')
        labels = {
        'username': 'Nome de Usuário',
        'password': 'Senha',
        'email': 'Email',
        'cpf': 'CPF',
        'telefone': 'Telefone',
    }
        widgets={
            'password': forms.PasswordInput()
}

class Atividade (forms.ModelForm): 
    class Meta: 
        model = Atividade
        fields  = ('nomeatividade', 'palestrante', 'duracao', 'data', 'tipo')
        labels = {
        'nomeatividade': 'Nome da Atividade',
        'palestrante': 'Palestrante',
        'duracao': 'Duração',
        'data': 'Data',
        'tipo': 'Tipo',
    }

class Evento(forms.ModelForm): 
    class Meta: 
        model = Eventos
        fields  = ('atividade', 'descricao', 'nome')
        labels = {
        'atividade': 'Atividade',
        'descricao': 'Descrição',
        'nome': 'Nome',
    }