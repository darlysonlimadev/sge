from django import forms
from .models import Categoria  # Importação direta do modelo


class CategoriaForm(forms.ModelForm):
    nome = forms.CharField(
        label="Nome",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da categoria'}),
    )

    descricao = forms.CharField(
        label="Descrição",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva a categoria'}),
        required=False  # Torna o campo opcional
    )

    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
