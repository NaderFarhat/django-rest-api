from rest_framework import serializers
from events.models import Event, Comitees

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