import json
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from events.models import Events, Noc
from events.api.serializers import EventsSerializer, NocSerializer

class CRUDTestCase(APITestCase):

    def setUp(self):
        noc_obj = Noc(        
            noc= "AHO",
            region= "Curacao",
            notes= "Netherlands Antilles"
        )
        noc_obj.save()
        evt_obj = Events(
            identification= 5,
            name= "Christine Jacoba Aaftink",
            sex= "F",
            age= 32,
            height= 182,
            weight= 60,
            team= "Netherlands",
            noc= Noc.objects.first() ,
            games= "1992 Summer",
            year= 1992,
            season= "Winter",
            city= "Barcelona",
            sport= "Basketball",
            event= "Basketball Men's Basketball",
            medal= "Gold"
        )
        evt_obj.save()
    
    def test_registration_noc(self):
        data = {
            "noc": "AHO",
            "region": "Curacao",
            "notes": "Netherlands Antilles"
        }
        response = self.client.post('/api/events/nocs/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_athletes(self):
        data = {
            "identification": 5,
            "name": "Christine Jacoba Aaftink",
            "sex": "F",
            "age": 32,
            "height": 182,
            "weight": 60,
            "team": "Netherlands",
            "noc": {
                "noc": "AHO",
                "region": "Curacao",
                "notes": "Netherlands Antilles"
            },
            "games": "1992 Summer",
            "year": 1992,
            "season": "Winter",
            "city": "Barcelona",
            "sport": "Basketball",
            "event": "Basketball Men's Basketball",
            "medal": "Gold"
        }

        response = self.client.post('/api/events/teste/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_only_one_noc(self):
        noc_count = Noc.objects.count()
        self.assertEqual(noc_count, 1)

    def test_only_one_athlete(self):
        events_count = Events.objects.count()
        self.assertEqual(events_count, 1)

    def test_get_list_noc(self):
        data = {}
        url = '/api/events/nocs/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_athletes(self):
        data = {}
        url = '/api/events/athletes/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_noc_invalid(self):
        data = {
            "noc": "AFG",
            "region": "",
            "notes":""
        }
        response = self.client.post('/api/events/nocs/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_athlete_invalid(self):
        data = {
            "identification": 5,
            "name": "",
            "sex": "",
            "age": 32,
            "height": 182,
            "weight": 60,
            "team": "Netherlands",
            "noc": {
                "noc": "AHO",
                "region": "Curacao",
                "notes": "Netherlands Antilles"
            },
            "games": "1992 Summer",
            "year": 1992,
            "season": "Winter",
            "city": "Barcelona",
            "sport": "Basketball",
            "event": "Basketball Men's Basketball",
            "medal": "Gold"
        }
        response = self.client.post('/api/events/teste/', data, format='json')
        self.assertEqual(response.status_code, 400)

    
