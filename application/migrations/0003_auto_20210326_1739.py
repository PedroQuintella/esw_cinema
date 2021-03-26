# Generated by Django 2.2.19 on 2021-03-26 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20210325_2341'),
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
                ('codigo', models.UUIDField(verbose_name='Código')),
                ('estado', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=100, verbose_name='UF')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('cep', models.CharField(help_text='Digite sem pontos e traços.', max_length=8, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.Usuario')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
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
                ('codigo', models.UUIDField(verbose_name='Código')),
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
            model_name='assento',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Sala'),
        ),
    ]