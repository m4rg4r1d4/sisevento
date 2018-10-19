from __future__ import unicode_literals
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'sisevento'

urlpatterns = [

	path ('', views.Home.as_view(), name='home'), 

	path ('cadastro/', views.UserCreateView.as_view(), name='cadastro'),

	path ('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

	path ('logout/', auth_views.LogoutView.as_view(), name='logout'),





















	# path('', views.HomeView.as_view(), name='home'),

	# path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

	# path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	
]