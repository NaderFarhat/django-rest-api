import json

from events.api.serializers import *
from events.models import Comitees, Event, Athlete, Game
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
            games= "1992 Summer",
            year= "1992",
            season= "Summer",
            city= "Barcelona",
        )
        evt_obj.save()
        game_obj = Game(
            sport= "Basketball",
            event= "Basketball Men's Basketball",
            medal= "NA"
        )
        game_obj.save()
        ath_obj = Athlete(
            name= "A Dijiang",
            sex= "M",
            age= "24",
            height= "123",
            weight= "132",
            noc= Comitees.objects.first(),
            event=Event.objects.first(),
            game=Game.objects.first()
        )
        ath_obj.save()

    def test_registration_com(self):
        data = {
            "noc": "AHO",
            "region": "Curacao",
            "notes": "Netherlands Antilles"
        }
        response = self.client.post('/api/events/com/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_game(self):
        data = {
            "sport": "asd",
            "event": "asd",
            "medal": "Gold"
        }
        response = self.client.post('/api/events/game/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_event(self):
        data = {        
            "games": "1992 summer",
            "year": "1992",
            "season": "summer",
            "city": "Barcelona"
        }
        response = self.client.post('/api/events/evt/', data)
        self.assertEqual(response.status_code, 201)

    def test_registration_athlete(self):
        data = {        
            "name": "A",
            "sex": "F",
            "age": "25",
            "height": "123",
            "weight": "132",
            "noc": {
                "noc": "BRA",
                "region": "SA",
                "notes": ""
            },
            "event": {
                "games": "QQ",
                "year": "2020",
                "season": "summer",
                "city": "Tokyo"
            },
            "game": {
                "sport": "Fute",
                "event": "liberta",
                "medal": "Gold"
            }
        }
        response = self.client.post('/api/events/ath/', data)
        self.assertEqual(response.status_code, 201)
        
    def test_only_one_comitee(self):
        noc_count = Comitees.objects.count()
        self.assertEqual(noc_count, 1)

    def test_only_one_game(self):
        game_count = Game.objects.count()
        self.assertEqual(game_count, 1)
    
    def test_only_one_comitee(self):
        evc_count = Event.objects.count()
        self.assertEqual(evc_count, 1)

    def test_only_one_athlete(self):
        ath_count = Athlete.objects.count()
        self.assertEqual(ath_count, 1)

    def test_get_list_comitee(self):
        data = {}
        url = '/api/events/com/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_game(self):
        data = {}
        url = '/api/events/game/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_event(self):
        data = {}
        url = '/api/events/evt/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_athlete(self):
        data = {}
        url = '/api/events/ath/'
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

    def test_create_game_invalid(self):
        data = {
            "sport": "",
            "event": "",
            "medal": "Gold"
        }
        response = self.client.post('/api/events/com/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_event_invalid(self):
        data = {
            "games": "",
            "year": "",
            "season": "summer",
            "city": ""
        }
        response = self.client.post('/api/events/evt/', data, format='json')
        self.assertEqual(response.status_code, 400)
    
    def test_delete_evt(self):
        delete_evt = Event.objects.last()
        url = delete_evt.get_api_url()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_delete_game(self):
        delete_game = Game.objects.last()
        url = delete_game.get_api_url()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_delete_comitee(self):
        delete_comitee = Comitees.objects.last()
        url = delete_comitee.get_api_url()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_delete_athlete(self):
        delete_athlete = Athlete.objects.last()
        url = delete_athlete.get_api_url()
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
            "games": "B",
            "year": "2018",
            "season": "summer",
            "city": "CWB"
        }
        update_evt = Event.objects.last()
        url = update_evt.get_api_url()
        response = self.client.put(url, data , format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_evt_partial_update(self):
        data = {"game":"teste"}
        patch_evt = Event.objects.first()
        url = patch_evt.get_api_url()
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
