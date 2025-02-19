from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):

    class Meta:
        model = Entrada
        fields = ['fornecedor', 'produto', 'quantidade', 'descricao']
        widgets = {
            'fornecedor': forms.Select(attrs={'class': 'form-control select2'}),
            'produto': forms.Select(attrs={'class': 'form-control select2'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Insira uma descrição opcional'
            }),
        }
        labels = {
            'fornecedor': 'Fornecedor',
            'produto': 'Produto',
            'quantidade': 'Quantidade',
            'descricao': 'Descrição',
        }

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade
