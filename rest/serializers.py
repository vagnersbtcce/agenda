'''
Serializer --> passagem do modelo Tarefa para JSON, que eh o formato
               protocolado para I/O de API
'''

from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('id', 'descricao', 'criacao', 'categoria', 'status')
