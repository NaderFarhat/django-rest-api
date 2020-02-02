from rest_framework import generics
from events.models import Event, Comitees
from .serializers import EventsSerializer, ComiteesSerializer
from .pagination import PostLimitOffsetPagination
from django_filters import rest_framework as filters

class EventAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = EventsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self):
        return Event.objects.all()
    

class EventRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EventsSerializer

    def get_queryset(self):
        return Event.objects.all()

class ComiteeAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = ComiteesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self):
        return Comitees.objects.all()

class ComiteeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ComiteesSerializer
    queryset = Comitees.objects.all()
        