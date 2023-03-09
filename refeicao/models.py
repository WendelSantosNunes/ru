from django.db import models
from funcionario.models import User



# Create your models here.

class Componente(models.Model):
    decricao = models.CharField(max_length=100, verbose_name='Descrição')
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.decricao


class Cardapio(models.Model):
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    almoco = models.ManyToManyField(Componente, related_name='tarde', blank=True,verbose_name='Almoço')
    jantar =  models.ManyToManyField(Componente,related_name='noite', blank=True)
    almocoVeg = models.ManyToManyField(Componente, related_name='Vegtarde', blank=True)
    jantarVeg =  models.ManyToManyField(Componente,related_name='Vegnoite', blank=True) 
    tem_almoco = models.BooleanField() 
    tem_jantar = models.BooleanField()
    data = models.DateField(unique = True, blank=False)
    funciona = models.BooleanField() 

    # def __str__(self):
    #     return self.funciona


class Comentario(models.Model):
    REFEICAO_CHOICES = (
        (1, 'Almoço'),
        (2, 'Almoço Vegetariano'),
        (3, 'Jantar'),
        (4, 'Jantar Vegetariano')
    )

    decricao = models.TextField()
    refeicao = models.IntegerField(choices=REFEICAO_CHOICES)
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)


class QtdRefeicao(models.Model):
    MES_CHOICES = [
        ("Janeiro", "Janeiro"),
        ("Fevereiro", "Fevereiro"),
        ("Março", "Março"),
        ("Abril", "Abril"),
        ("Maio", "Maio"),
        ("Junho", "Junho"),
        ("Julho", "Julho"),
        ("Agosto", "Agosto"),
        ("Setembro", "Setembro"),
        ("Outubro", "Outubro"),
        ("Novembro", "Novembro"),
        ("Dezembro", "Dezembro"),
    ]
    ANO_CHOICES = [
        (str(i), str(i)) for i in range(2023, 2100)
    ]
    mes = models.CharField(max_length=20, choices=MES_CHOICES)
    ano = models.CharField(max_length=4, choices=ANO_CHOICES)
    almocoQtd = models.IntegerField()
    jantarQtd = models.IntegerField()

    
