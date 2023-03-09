from datetime import date
from wsgiref.validate import validator
from xml.dom import ValidationErr
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# from django.core.validators import validate_email


class UsuarioForm(UserCreationForm):


    def clean_email(self):
        nome, dominio = self.cleaned_data['email'].rsplit('@', 1)

        if dominio == 'ufpi.edu.br':
            return self.cleaned_data['email']
        else:
            raise ValidationErr('Necessário um Email institucional UFPI!')


    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']

        if len(matricula) == 7:
            if matricula.isdigit():
                return self.cleaned_data['matricula']
        raise ValidationErr('matricula inválida!')

 
