from django.contrib import admin
from .models import Entrada

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('fornecedor', 'produto', 'quantidade', 'created_at', 'updated_at',)
    search_fields = ('fornecedor__nome', 'produto__nome',)

