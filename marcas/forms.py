from django import forms
from . import models

class MarcaForm(forms.ModelForm):

    class Meta:
        model = models.Marca
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
        }