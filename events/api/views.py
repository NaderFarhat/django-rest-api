from rest_framework import generics
from events.models import Events, Noc
from .serializers import EventsSerializer, NocSerializer
from django_filters import rest_framework as filters


class EventFilterView(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class EventAPIView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = EventsSerializer

    def get_queryset(self):
        return Events.objects.all()

class EventRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EventsSerializer

    def get_queryset(self):
        return Events.objects.all()
        
class NocFilterView(generics.ListCreateAPIView):
    queryset = Noc.objects.all()
    serializer_class = NocSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class NocAPIView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = NocSerializer

    def get_queryset(self):
        return Noc.objects.all()

class NocRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = NocSerializer

    def get_queryset(self):
        return Noc.objects.all()