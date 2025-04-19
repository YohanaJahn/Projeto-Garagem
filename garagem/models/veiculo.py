from django.db import models
from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT,blank=False,null=False)
    cor = models.ForeignKey(Cor,on_delete=models.PROTECT ,blank=False,null=False)
    acessorio = models.ManyToManyField(Acessorio, blank=True)

    def __str__(self):
        return f"({self.id}) {(self.modelo)} {self.cor} {self.ano} "