from garagem.models import Acessorio
from garagem.serializers import AcessorioSerializer
from rest_framework import viewsets

class AcessorioViewSet(viewsets.ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer