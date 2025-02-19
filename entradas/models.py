from django.db import models
from produtos.models import Produto
from fornecedores.models import Fornecedor
from django.core.validators import MinValueValidator


class Entrada(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='entradas')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='entradas')
    quantidade = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    descricao = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.produto} - {self.quantidade} unidades ({self.created_at.strftime('%d/%m/%Y')})"

