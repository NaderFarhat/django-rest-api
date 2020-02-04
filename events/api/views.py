from rest_framework import generics
from events.models import Event, Comitees, Athlete
from .serializers import EventsSerializer, ComiteesSerializer, AthleteSerializer
from .pagination import PostLimitOffsetPagination
from django_filters import rest_framework as filters
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response


class ApiRootView(APIView):
    def get(self, request):
        data = {
            'list-comitees': reverse_lazy('api-events:com-list', request=request),
            'list-events': reverse_lazy('api-events:event-list', request=request),
            'list-athletes': reverse_lazy('api-events:athlete-list', request=request),
        }
        return Response(data)

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

class AthleteAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = AthleteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self):
        return Athlete.objects.all()

class AthleteRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all()
        