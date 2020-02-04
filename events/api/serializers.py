from rest_framework import serializers
from events.models import Event, Comitees, Athlete, Game
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

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'sport',
            'event',
            'medal'
        ]


class EventsSerializer(WritableNestedModelSerializer):
    
    class Meta:
        model = Event
        fields = [
            'id',
            'games',
            'year',
            'season',
            'city'
        ]

class AthleteSerializer(WritableNestedModelSerializer):
    noc = ComiteesSerializer(many=False)
    event = EventsSerializer(many=False)
    game = GameSerializer(many=False)

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
            'event',
            'game'
        ]
