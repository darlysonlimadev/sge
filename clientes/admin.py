from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'cpf', 'data_nascimento', 'cep', 'endereco', 'bairro', 'numero',
                    'complemento', 'bairro', 'numero', 'cidade', 'estado', 'created_at', 'operador_created_id',
                    'updated_at', 'operador_updated_id')
    search_fields = ('nome', 'cpf',)