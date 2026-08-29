from django.db import models

class Moeda(models.Model):
    codigo = models.CharField(max_length=10, unique=True)  
    nome = models.CharField(max_length=100)  

    def __str__(self):
        return self.codigo


class Conversao(models.Model):
    moeda_origem = models.ForeignKey(Moeda, related_name='conversoes_origem', on_delete=models.CASCADE)
    moeda_destino = models.ForeignKey(Moeda, related_name='conversoes_destino', on_delete=models.CASCADE)
    valor_original = models.DecimalField(max_digits=15, decimal_places=2)
    valor_convertido = models.DecimalField(max_digits=15, decimal_places=2)
    data_conversao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.valor_original} {self.moeda_origem.codigo} -> {self.valor_convertido} {self.moeda_destino.codigo}'

# Create your models here.
