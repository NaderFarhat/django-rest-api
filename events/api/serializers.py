from rest_framework import serializers
from events.models import Event, Comitees, Athlete
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

class EventsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = [
            'id',
            'team',
            'games',
            'year', 
            'season', 
            'city', 
            'sport',
            'event',
            'medal'
        ]

class AthleteSerializer(WritableNestedModelSerializer):
    noc = ComiteesSerializer(many=False)
    event = EventsSerializer(many=False)

    class Meta:
        model = Athlete
        fields = [
            'id',
            'name',
            'sex',
            'age',
            'height',
            'weight',
            'noc',
            'event'
        ]
