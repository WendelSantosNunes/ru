from datetime import date
from xml.dom import ValidationErr
from .models import Cardapio, Comentario, Componente, QtdRefeicao
from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple


class CardapioForm(ModelForm):
    almoco = ModelMultipleChoiceField( 
        queryset=Componente.objects.all().order_by('decricao'),
        widget=CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label = 'Almoço'
    )
    almocoVeg = ModelMultipleChoiceField(
        queryset=Componente.objects.all().order_by('decricao'),
        widget=CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label = 'Almoço Vegetariano'
    )
    jantar = ModelMultipleChoiceField(
        queryset=Componente.objects.all().order_by('decricao'),
        widget=CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )
    jantarVeg = ModelMultipleChoiceField(
        queryset=Componente.objects.all().order_by('decricao'),
        widget=CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label = 'Jantar Vegetariano'
    )
    tem_almoco = forms.BooleanField(widget=forms.RadioSelect(choices=((True, 'Sim'), (False, 'Não'))))
    
    tem_jantar = forms.BooleanField(widget=forms.RadioSelect(choices=((True, 'Sim'), (False, 'Não'))))
    
    funciona = forms.BooleanField(widget=forms.RadioSelect(choices=((True, 'Sim'), (False, 'Não'))))
        
    # data = forms.DateField(widget=forms.TextInput(attrs={'type': "date"}))

    data = forms.DateField(widget=forms.TextInput(attrs={'type': "date"}),error_messages={'invalid': 'Data inválida.'})
    # tem_almoco = forms.BooleanField(label='Tem Almoço?')
    # tem_jantar = forms.BooleanField(label='Tem jantar?')

    def clean_data(self):
        data = self.cleaned_data['data']
        atual = date.today()

        if int((data - atual).total_seconds() // 3600) > 0:
            return self.cleaned_data['data']
        else:
            # raise ValidationErr('erro')
            raise ValidationErr('Data inválida.')


    class Meta:
        model = Cardapio
        fields = ['almoco', 'jantar', 'almocoVeg', 'jantarVeg', 'data', 'tem_almoco', 'tem_jantar']

        widgets = {
            'almoco': forms.TextInput(attrs={"placeholder": 'Almoço'}),
            'almocoVeg': forms.TextInput(attrs={"placeholder": 'Almoço Vegetariano'}),
            'jantar': forms.TextInput(attrs={"placeholder": 'Jantar'}),
            'jantarVeg': forms.TextInput(attrs={"placeholder": 'Jantar Vegetariano'}),
   }

class ComponenteForm(forms.ModelForm):
# VERIFICAR TESTE
    def clean_decricao(self):
        return self.cleaned_data['decricao'].upper()


    class Meta:
        model = Componente
        fields = ['decricao']

        widgets = {
            'decricao': forms.TextInput(attrs={"placeholder": 'Componente'})
        }



class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['decricao', 'refeicao', 'cardapio']

        cardapios = Cardapio.objects.all()
        array = []
        datas = [(cardapio.data, cardapio.data.strftime('%d/%m/%Y')) for cardapio in cardapios]

        for item in cardapios:
            array.append(item.data)

        widgets = {
            'decricao': forms.TextInput(attrs={"placeholder": 'Comentário'}),
            'refeicao': forms.Select(attrs={"class": "form-select"}),
            'cardapio': forms.Select(choices=datas, attrs={"class": "form-select"}),
        }

        labels = {
            'descricao': 'Descrição',
            'refeicao': 'Refeição',
            'cardapio': 'Cardápio',
        }
        
class QtdRefeicaoForm(ModelForm):
    class Meta:
        model = QtdRefeicao
        fields = ['mes', 'ano', 'almocoQtd', 'jantarQtd']

        labels = {
            'mes': 'Mês',
            'almocoQtd': 'Almoço',
            'jantarQtd': 'Jantar',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        mes = cleaned_data.get('mes')
        ano = cleaned_data.get('ano')
        
        # Verifica se já existe uma instância com o mesmo mês e ano
        qtd_refeicao_existente = QtdRefeicao.objects.filter(mes=mes, ano=ano)
        print("existe: ", qtd_refeicao_existente)
        if qtd_refeicao_existente.exists():
            raise ValidationErr('Já existe uma quantidade de refeições para o mês e ano selecionados.')


class UpdateRefeicaoForm(ModelForm):
    class Meta:
        model = QtdRefeicao
        fields = ['almocoQtd', 'jantarQtd']

        labels = {
            'almocoQtd': 'Almoço',
            'jantarQtd': 'Jantar',
        }
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     mes = cleaned_data.get('mes')
    #     ano = cleaned_data.get('ano')
        
    #     # Verifica se já existe uma instância com o mesmo mês e ano
    #     qtd_refeicao_existente = QtdRefeicao.objects.filter(mes=mes, ano=ano)
    #     print("existe: ", qtd_refeicao_existente)
    #     if not qtd_refeicao_existente:
    #         raise ValidationErr('Já existe uma quantidade de refeições para o mês e ano selecionados.')