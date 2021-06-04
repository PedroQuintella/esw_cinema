from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _


class ContatoForm(forms.Form):
    nome = forms.CharField(label=_('Nome'), max_length=100)
    email = forms.EmailField(label=_('E-mail'), max_length=100)
    assunto = forms.CharField(label=_('Assunto'), max_length=100)
    mensagem = forms.CharField(label=_('Mensagem'), widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@dominio.com.br',
            to=['contato@dominio.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()
