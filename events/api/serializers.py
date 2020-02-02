from rest_framework import serializers
from events.models import Event, Comitees
from drf_writable_nested.serializers import WritableNestedModelSerializer

class ComiteesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comitees
        fields = [
            'id',
            'noc',
            'region',
            'notes'
        ]

class EventsSerializer(WritableNestedModelSerializer):
    noc = ComiteesSerializer(many=False)
    
    class Meta:
        model = Event
        fields = [
            'id',
            'identification',
            'name',
            'sex',
            'age',
            'height',
            'weight',
            'team',
            'noc',
            'games',
            'year',
            'season',
            'city',
            'sport',
            'event',
            'medal',

        ]