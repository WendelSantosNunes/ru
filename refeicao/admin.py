from django.contrib import admin
from .models import Componente, Cardapio, Comentario, QtdRefeicao
# Register your models here.
from django.utils.html import format_html
from django.urls import reverse
from datetime import date
from django.db.models import Sum

class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('id','decricao',)

    # display_link 

class CardapioAdmin(admin.ModelAdmin):
    list_display = ('id', 'list_almoco', 'list_jantar', 'list_almocoVeg', 'list_jantarVeg',)
    
    def list_almoco(self, obj):
        return ", ".join([str(ing) for ing in obj.almoco.all()])
    list_almoco.short_description = 'Almoço'
    
    def list_jantar(self, obj):
        return ", ".join([str(ing) for ing in obj.jantar.all()])
    list_jantar.short_description = 'Jantar'
    
    def list_almocoVeg(self, obj):
        return ", ".join([str(ing) for ing in obj.almocoVeg.all()])
    list_almocoVeg.short_description = 'Almoço Vegetariano'
    
    def list_jantarVeg(self, obj):
        return ", ".join([str(ing) for ing in obj.jantarVeg.all()])
    list_jantarVeg.short_description = 'Jantar Vegerariano'
    
    # display_link 
class QtdRefeicaoAdmin(admin.ModelAdmin):
    list_display = ('mes', 'ano', 'almocoQtd', 'jantarQtd')

    # def refeicoes_servidas(self, obj):
    #     ano_atual = date.today().year
    #     qtd_refeicoes = QtdRefeicao.objects.filter(ano=ano_atual).aggregate(Sum('almocoQtd'), Sum('jantarQtd'))
    #     almoco_servido = qtd_refeicoes['almocoQtd__sum'] or 0
    #     jantar_servido = qtd_refeicoes['jantarQtd__sum'] or 0
    #     return format_html('<a href="{}">{}</a>', reverse('admin:qtdrefeicao_qtdrefeicao_changelist'), f'{almoco_servido} almoços, {jantar_servido} jantares servidos este ano')
    
#     refeicoes_servidas.short_description = 'Refeições Servidas'

admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Cardapio, CardapioAdmin)
admin.site.register(Comentario)
admin.site.register(QtdRefeicao, QtdRefeicaoAdmin)


