from garagem.models import Cor
from garagem.serializers import CorSerializer
from rest_framework import viewsets

class CorViewSet(viewsets.ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer