#coding:utf-8

from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import UUIDUser, Atividade

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
        fields  = ('palestrante', 'duracao', 'data', 'tipo')
        labels = {
        'palestrante': 'Palestra',
        'duracao': 'Duração',
        'data': 'Data',
        'tipo': 'Tipo',
    }