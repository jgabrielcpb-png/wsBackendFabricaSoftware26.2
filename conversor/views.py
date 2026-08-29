import requests
from django.shortcuts import render
from rest_framework import viewsets, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Moeda, Conversao
from .serializers import MoedaSerializer, ConversaoSerializer


class MoedaViewSet(viewsets.ModelViewSet):
    queryset = Moeda.objects.all()
    serializer_class = MoedaSerializer


class ConversaoInputSerializer(serializers.Serializer):
    moeda_origem = serializers.CharField(max_length=10)
    moeda_destino = serializers.CharField(max_length=10)
    valor = serializers.FloatField()


class ConversaoView(APIView):
    @extend_schema(request=ConversaoInputSerializer, responses=ConversaoSerializer)
    def post(self, request):
        moeda_origem = request.data.get('moeda_origem')
        moeda_destino = request.data.get('moeda_destino')
        valor = request.data.get('valor')

        if not moeda_origem or not moeda_destino or not valor:
            return Response(
                {'erro': 'Informe moeda_origem, moeda_destino e valor.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            valor = float(valor)
        except ValueError:
            return Response(
                {'erro': 'O valor deve ser numérico.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        par = f'{moeda_origem.upper()}-{moeda_destino.upper()}'
        url = f'https://economia.awesomeapi.com.br/json/last/{par}'

        try:
            resposta = requests.get(url, timeout=5)
            resposta.raise_for_status()
        except requests.exceptions.RequestException:
            return Response(
                {'erro': 'Não foi possível consultar a cotação. Tente novamente mais tarde.'},
                status=status.HTTP_502_BAD_GATEWAY
            )

        dados = resposta.json()
        chave = f'{moeda_origem.upper()}{moeda_destino.upper()}'

        if chave not in dados:
            return Response(
                {'erro': 'Par de moedas inválido.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        cotacao = float(dados[chave]['bid'])
        valor_convertido = valor * cotacao

        origem_obj, _ = Moeda.objects.get_or_create(codigo=moeda_origem.upper(), defaults={'nome': moeda_origem.upper()})
        destino_obj, _ = Moeda.objects.get_or_create(codigo=moeda_destino.upper(), defaults={'nome': moeda_destino.upper()})

        conversao = Conversao.objects.create(
            moeda_origem=origem_obj,
            moeda_destino=destino_obj,
            valor_original=valor,
            valor_convertido=valor_convertido
        )

        serializer = ConversaoSerializer(conversao)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    

# Create your views here.
