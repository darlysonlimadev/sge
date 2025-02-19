from rest_framework import serializers
from fornecedores.models import Fornecedor


class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fornecedor
        fields = '__all__'
