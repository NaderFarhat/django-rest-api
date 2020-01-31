from rest_framework import serializers
from events.models import Events, Noc
from drf_writable_nested.serializers import WritableNestedModelSerializer

class NocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noc
        fields = [
            'id',
            'noc',
            'region',
            'notes'
        ]

class EventsSerializer(WritableNestedModelSerializer):
    noc = NocSerializer(many=False)
    
    class Meta:
        model = Events
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

        

