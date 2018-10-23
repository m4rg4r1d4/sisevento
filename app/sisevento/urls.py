from __future__ import unicode_literals
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'sisevento'

urlpatterns = [

	path ('', views.Home.as_view(), name='home'), 

	path ('cadastro/', views.UserCreateView.as_view(), name='cadastro'),

	path ('atividade/', views.Atividade.as_view(), name='atividade'),

	path ('veratividade/', views.Veratividade.as_view(), name='veratividade'),

	path ('eventos/', views.Eventos.as_view(), name='eventos'),

	path ('listareventos/', views.ListEvento.as_view(), name='listareventos'),

	path ('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

	path ('logout/', auth_views.LogoutView.as_view(), name='logout'),

]