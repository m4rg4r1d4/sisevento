# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import uuid
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission

# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    # core
    cpf = models.IntegerField(verbose_name="CPF")
    telefone = models.IntegerField(verbose_name="telefone")


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Atividade(models.Model):
    types = (
    (1, 'Palestra'),
    (2, 'Minicurso')
)
    nomeatividade = models.CharField (max_length = 100, verbose_name='Nome da Atividade')
    criador = models.ForeignKey (UUIDUser, on_delete = models.CASCADE, related_name='atividade', verbose_name='criador')
    palestrante = models.CharField (max_length = 100, verbose_name='Criador')
    duracao = models.CharField (max_length = 100, verbose_name='Duração')
    data = models.DateTimeField (auto_now = False, auto_now_add = False)
    tipo = models.IntegerField (choices = types)

    def __str__(self):
        return self.nomeatividade

class Eventos (models.Model):
    criador = models.ForeignKey (UUIDUser, on_delete = models.CASCADE, related_name='eventos', verbose_name='criador')
    atividade = models.ForeignKey (Atividade, on_delete = models.CASCADE, related_name='eventos', verbose_name='atividade')
    descricao = models.TextField (verbose_name='Descricao')
    nome = models.CharField (max_length = 100, verbose_name='Nome')