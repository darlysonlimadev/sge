from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'marca', 'descricao', 'codigo', 'preco_custo', 'preco_venda']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição do produto'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código do produto'}),
            'preco_custo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'R$ 0,00'}),
            'preco_venda': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'R$ 0,00'}),
        }
        labels = {
            'nome': 'Nome',
            'categoria': 'Categoria',
            'marca': 'Marca',
            'descricao': 'Descrição',
            'codigo': 'Código',
            'preco_custo': 'Preço de Custo',
            'preco_venda': 'Preço de Venda',
        }
