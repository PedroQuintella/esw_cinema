from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('Email', unique=True)
    senha = models.CharField('Senha', max_length=30)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome




