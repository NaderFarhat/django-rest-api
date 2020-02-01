from rest_framework import generics
from events.models import Event, Comitees
from .serializers import EventsSerializer, ComiteesSerializer
from django_filters import rest_framework as filters

class EventFilterView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class EventAPIView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = EventsSerializer

    def get_queryset(self):
        return Event.objects.all()


class EventRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EventsSerializer

    def get_queryset(self):
        return Event.objects.all()


class ComiteesFilterView(generics.ListCreateAPIView):
    queryset = Comitees.objects.all()
    serializer_class = ComiteesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ComiteeAPIView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = ComiteesSerializer

    def get_queryset(self):
        return Comitees.objects.all()


class ComiteeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ComiteesSerializer

    def get_queryset(self):
        return Comitees.objects.all()
        