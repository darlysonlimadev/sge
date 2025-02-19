from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'marca', 'preco_venda', 'quantidade', 'created_at')
    search_fields = ('nome',)
