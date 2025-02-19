from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    nome = forms.CharField(
        label="Nome",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da categoria'}),
    )

    descricao = forms.CharField(
        label="Descrição",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva a categoria'}),
        required=False
    )

    class Meta:
        model = Fornecedor
        fields = ['nome', 'descricao']

    def clean_nome(self):
        nome = self.cleaned_data.get("nome")
        if nome.strip() == "":
            raise forms.ValidationError("O nome não pode ser vazio ou conter apenas espaços.")
        return nome

