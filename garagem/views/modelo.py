from garagem.models import Modelo
from garagem.serializers import ModeloSerializer
from rest_framework import viewsets

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer