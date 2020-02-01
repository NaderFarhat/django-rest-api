import json

from events.api.serializers import ComiteesSerializer, EventsSerializer
from events.models import Comitees, Event
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase


class CRUDTestCase(APITestCase):

    def setUp(self):
        noc_obj = Comitees(        
            noc= "AHO",
            region= "Curacao",
            notes= "Netherlands Antilles"
        )
        noc_obj.save()
        evt_obj = Event(
            identification= 5,
            name= "Christine Jacoba Aaftink",
            sex= "F",
            age= 32,
            height= 182,
            weight= 60,
            team= "Netherlands",
            noc= Comitees.objects.first() ,
            games= "1992 Summer",
            year= 1992,
            season= "Winter",
            city= "Barcelona",
            sport= "Basketball",
            event= "Basketball Men's Basketball",
            medal= "Gold"
        )
        evt_obj.save()

    def test_registration_com(self):
        data = {
            "noc": "AHO",
            "region": "Curacao",
            "notes": "Netherlands Antilles"
        }
        response = self.client.post('/api/events/com/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_event(self):
        data = {        
            "identification": 5,
            "name": "Christine Jacoba Aaftink",
            "sex": "F",
            "age": "32",
            "height": "182",
            "weight": "60",
            "team": "Netherlands",
            "noc": {
                "noc": "AHO",
                "region": "Curacao",
                "notes": "Netherlands Antilles"
            },
            "games": "1992 Summer",
            "year": "1992",
            "season": "Winter",
            "city": "Barcelona",
            "sport": "Basketball",
            "event": "Basketball Men's Basketball",
            "medal": "Gold"
        }

        response = self.client.post('/api/events/evt/', data)
        self.assertEqual(response.status_code, 201)
        
    def test_only_one_comitee(self):
        noc_count = Comitees.objects.count()
        self.assertEqual(noc_count, 1)

    def test_only_one_event(self):
        events_count = Event.objects.count()
        self.assertEqual(events_count, 1)

    def test_get_list_comitee(self):
        data = {}
        url = '/api/events/com/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_event(self):
        data = {}
        url = '/api/events/evt/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_com_invalid(self):
        data = {
            "noc": "AFG",
            "region": "",
            "notes":""
        }
        response = self.client.post('/api/events/com/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_event_invalid(self):
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
        response = self.client.post('/api/events/evt/', data, format='json')
        self.assertEqual(response.status_code, 400)
    
    def test_delete_evt(self):
        Event.objects.create(
            identification=5,
            name="Christine Jacoba Aaftink",
            sex="F",
            age="32",
            height="182",
            weight="60",
            team="Netherlands",
            noc=Comitees.objects.create(noc="AHO", region="Curacao", notes="Netherlands Antilles"),
            games="1992 Summer",
            year="1992",
            season="Winter",
            city="Barcelona",
            sport="Basketball",
            event="Basketball Men's Basketball",
            medal="Gold"
        )
        delete_evt = Event.objects.last()
        url = delete_evt.get_api_url()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_delete_comitee(self):
        new_comitee = Comitees.objects.create(
                noc="BRA",
                region="TES",
                notes=""
            )
        delete_comitee = Comitees.objects.last()
        url = delete_comitee.get_api_url()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_com_update(self):
        data = {"noc": "test", "region": "tes", "notes":" "}
        update_comitee = Comitees.objects.last()
        url = update_comitee.get_api_url()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_com_partial_update(self):
        data = {"noc": "test"}
        patch_comitee = Comitees.objects.first()
        url = patch_comitee.get_api_url()
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_evt_update(self):
        data = {        
            "identification": 5,
            "name": "Christine Jacoba Aaftink",
            "sex": "F",
            "age": "32",
            "height": "182",
            "weight": "60",
            "team": "Netherlands",
            "noc": {
                "noc": "AHO",
                "region": "Curacao",
                "notes": "Netherlands Antilles"
            },
            "games": "1992 Summer",
            "year": "1992",
            "season": "Winter",
            "city": "Barcelona",
            "sport": "Basketball",
            "event": "Basketball Men's Basketball",
            "medal": "Gold"
        }
        update_evt = Event.objects.last()
        url = update_evt.get_api_url()
        response = self.client.put(url, data , format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_evt_partial_update(self):
            data = {"name":"teste"}
            patch_evt = Event.objects.first()
            url = patch_evt.get_api_url()
            response = self.client.patch(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)