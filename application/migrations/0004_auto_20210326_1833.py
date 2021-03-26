# Generated by Django 2.2.19 on 2021-03-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20210326_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ingresso',
            name='id',
        ),
        migrations.AlterField(
            model_name='compra',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='ingresso',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Código'),
        ),
    ]
