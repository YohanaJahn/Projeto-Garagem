from garagem.models import Veiculo
from garagem.serializers import VeiculoSerializer
from rest_framework import viewsets

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer