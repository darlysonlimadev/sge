from rest_framework import serializers
from entradas.models import Entrada


class EntradaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entrada
        fields = '__all__'
