from rest_framework import serializers
from .models import Moeda, Conversao

class MoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        fields = '__all__'


class ConversaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversao
        fields = '__all__'