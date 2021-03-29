# Generated by Django 2.2.19 on 2021-03-29 20:45

import application.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Assento')),
            ],
            options={
                'verbose_name': 'Assento',
                'verbose_name_plural': 'Assentos',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(verbose_name='Código')),
                ('estado', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=100, verbose_name='UF')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('cep', models.CharField(help_text='Digite sem pontos e traços.', max_length=8, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('cartaz', stdimage.models.StdImageField(blank=True, null=True, upload_to=application.models.get_file_path, verbose_name='Cartaz')),
                ('sinopse', models.TextField(max_length=1000, verbose_name='Sinopse')),
                ('trailer', models.URLField(blank=True, null=True, verbose_name='Trailer')),
                ('dataEstreia', models.DateField(blank=True, help_text='Use este formato: DD/MM/AAAA', null=True, verbose_name='Data de Estreia')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(help_text='Digite sem pontos e traços.', max_length=11, unique=True, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('senha', models.CharField(max_length=30, verbose_name='Senha')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='Use este formato: DD/MM/AAAA', verbose_name='Data')),
                ('horario', models.TimeField(help_text='Use este formato: HH:MM', verbose_name='Horário')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Filme')),
                ('sala', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Sala')),
            ],
            options={
                'verbose_name': 'Sessão',
                'verbose_name_plural': 'Sessões',
            },
        ),
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(verbose_name='Código')),
                ('assento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Assento')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.Compra')),
                ('sala', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Sala')),
                ('sessao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Sessao')),
            ],
            options={
                'verbose_name': 'Ingresso',
                'verbose_name_plural': 'Ingressos',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.Usuario'),
        ),
        migrations.AddField(
            model_name='assento',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Sala'),
        ),
    ]
