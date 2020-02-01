from rest_framework import generics
from events.models import Event, Comitees
from .serializers import EventsSerializer, ComiteesSerializer

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