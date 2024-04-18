from rest_framework import viewsets
from .models import Run, RunData
from myapp.serializers import RunSerializer, RunDataSerializer

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

class RunDataViewSet(viewsets.ModelViewSet):
    queryset = RunData.objects.all()
    serializer_class = RunDataSerializer


