from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from .forms import CardapioForm, ComponenteForm, ComentarioForm, QtdRefeicaoForm, UpdateRefeicaoForm
from django.urls import reverse, reverse_lazy
from .models import Cardapio,Comentario,Componente, QtdRefeicao
from django.http import HttpResponse
from datetime import date, datetime
from django.db.models import Sum


class Sobre(TemplateView):
    template_name = 'main/sobre.html'

class CardapioView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['cardapios'] = Cardapio.objects.all()
        cardapio = Cardapio.objects.filter(data=date.today()).first()

        if cardapio:
            context['almoco'] = cardapio.almoco.all()
            context['jantar'] = cardapio.jantar.all()
            context['almoco_veg']  = cardapio.almocoVeg.all()
            context['jantar_veg'] = cardapio.jantarVeg.all()    
        
        # Obtém o ano corrente
        ano_corrente = datetime.now().year

        # Soma as refeições de almoço e jantar do ano corrente
        refeicoes = QtdRefeicao.objects.filter(ano=ano_corrente).aggregate(
            total_almoco=Sum('almocoQtd'),
            total_jantar=Sum('jantarQtd')
        )

        context['almoco_Qtd'] = refeicoes['total_almoco'] or 0
        context['jantar_Qtd'] = refeicoes['total_jantar'] or 0

        return context

    
class CardapioCreate(CreateView):
    # falta saber que pag vai voltar qnd terminar
    template_name = 'refeicao/criar-cardapio.html'
    form_class = CardapioForm
    success_url = reverse_lazy('lista-cardapio')
    
    def form_valid(self, form):

        form.instance.usuario = self.request.user
        form.instance.funciona = True

        # Antes do super não foi criado objeto

        url = super().form_valid(form)

        # Depois do super o objeto está criado
        return url 


class CardapioUpdate(UpdateView):
    model = Cardapio
    form_class = CardapioForm
    template_name = 'refeicao/criar-cardapio.html'
    success_url = reverse_lazy('lista-cardapio')


class CardapioDelete(DeleteView):
    model = Cardapio
    template_name = 'refeicao/deletar-cardapio.html'
    success_url = reverse_lazy('lista-cardapio')

class ComponenteView(TemplateView):
    template_name = 'componente/componente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listaComponente'] = Componente.objects.all().order_by('decricao')
        return context  

class ComponenteCreate(CreateView):
    success_url = reverse_lazy('home')
    template_name = 'componente/criar-componente.html'
    form_class = ComponenteForm

class ComponenteUpdate(UpdateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'componente/criar-componente.html'
    success_url = reverse_lazy('lista-componente')

class ComponenteDelete(DeleteView):
    model = Componente
    template_name = 'componente/deletar-componente.html'
    success_url = reverse_lazy('lista-componente')


class ComentarioView(TemplateView):
    template_name = 'comentario/comentario.html'

class ComentarioCreate(CreateView):
    success_url = reverse_lazy('home')
    template_name = 'comentario/criar-comentario.html'
    form_class = ComentarioForm
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['cardapios'] = Cardapio.objects.all()

    #     print(context['cardapios'].data)
    #     return context
    # cardapios = Cardapio.objects.all()
    # datas = [(cardapio.data, cardapio.data.strftime('%d/%m/%Y')) for cardapio in cardapios]

    # return render(request, 'criar_comentario.html', {'form': form_class, 'datas': datas})

class QtdRefeicaoView(TemplateView):
    template_name = 'qtd-refeicao/qtdrefeicao.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listaQtdRefeicao'] = QtdRefeicao.objects.values()

        print(context['listaQtdRefeicao'])

        return context

class QtdRefeicaoCreate(CreateView):
    success_url = reverse_lazy('qtdrefeicao')
    template_name = 'qtd-refeicao/criar-qtdrefeicao.html'
    form_class = QtdRefeicaoForm

class QtdRefeicaoUpdate(UpdateView):
    model = QtdRefeicao
    form_class = UpdateRefeicaoForm
    template_name = 'qtd-refeicao/criar-qtdrefeicao.html'
    success_url = reverse_lazy('qtdrefeicao')

class QtdRefeicaoDelete(DeleteView):
    model = QtdRefeicao
    template_name = 'qtd-refeicao/deletar-qtdrefeicao.html'
    success_url = reverse_lazy('qtdrefeicao')

class ListaCardapio(TemplateView):
    template_name = 'refeicao/lista-cardapio.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listaCardapios'] = Cardapio.objects.filter(data__gte=date.today()).order_by('data')[:5]
        return context


