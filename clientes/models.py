from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^\d{10,11}$', message="Somente números, com DDD")]
    )
    email = models.EmailField(null=True, blank=True)
    cpf = models.CharField(
        max_length=11,  # Apenas números
        unique=True,
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^\d{11}$', message="Digite apenas números (11 dígitos)")]
    )
    data_nascimento = models.DateField(null=True, blank=True)
    cep = models.CharField(
        max_length=8,  # Apenas números
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^\d{8}$', message="Digite apenas números (8 dígitos)")]
    )
    endereco = models.CharField(max_length=255, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    updated_at = models.DateTimeField(auto_now=True)  # Última atualização
    operador_created = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="clientes_criados"
    )  # Usuário que criou
    operador_updated = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="clientes_atualizados"
    )  # Usuário que atualizou

    def __str__(self):
        return self.nome

    def formatar_cpf(self):
        """Retorna o CPF formatado (XXX.XXX.XXX-XX)"""
        if self.cpf and len(self.cpf) == 11:
            return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return self.cpf

    def formatar_cep(self):
        """Retorna o CEP formatado (XXXXX-XXX)"""
        if self.cep and len(self.cep) == 8:
            return f"{self.cep[:5]}-{self.cep[5:]}"
        return self.cep
