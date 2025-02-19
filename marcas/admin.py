from django.contrib import admin
from .models import Marca

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'created_at', 'updated_at')  # Define os campos visíveis na listagem
    search_fields = ('nome',)  # Permite busca pelo nome
    list_filter = ('created_at',)  # Adiciona um filtro lateral por data de criação
    ordering = ('nome',)  # Ordena os registros pelo nome
