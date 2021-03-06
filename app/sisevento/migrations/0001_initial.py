# Generated by Django 2.0.7 on 2018-10-23 15:23

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUIDUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('telefone', models.IntegerField(verbose_name='telefone')),
                ('groups', models.ManyToManyField(blank=True, related_name='uuiduser_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='uuiduser_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeatividade', models.CharField(max_length=100, verbose_name='Nome da Atividade')),
                ('palestrante', models.CharField(max_length=100, verbose_name='Criador')),
                ('duracao', models.CharField(max_length=100, verbose_name='Duração')),
                ('data', models.DateTimeField()),
                ('tipo', models.IntegerField(choices=[(1, 'Palestra'), (2, 'Minicurso')])),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividade', to=settings.AUTH_USER_MODEL, verbose_name='criador')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descricao')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='sisevento.Atividade', verbose_name='atividade')),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to=settings.AUTH_USER_MODEL, verbose_name='criador')),
            ],
        ),
    ]
