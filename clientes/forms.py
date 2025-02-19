from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'telefone', 'email', 'cpf', 'data_nascimento', 'cep', 'endereco',
            'complemento', 'bairro', 'numero', 'cidade', 'estado',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do cliente'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(DDD) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o e-mail'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CEP'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o endereço'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o complemento'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o bairro'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número da residência'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o estado'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'cpf': 'CPF',
            'data_nascimento': 'Data de Nascimento',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'numero': 'Número',
            'cidade': 'Cidade',
            'estado': 'UF do Estado',
        }
