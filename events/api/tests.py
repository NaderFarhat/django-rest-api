import json

from events.api.serializers import ComiteesSerializer, EventsSerializer, AthleteSerializer
from events.models import Comitees, Event, Athlete
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
            team= "Netherlands",
            games= "1992 Summer",
            year= 1992,
            season= "Winter",
            city= "Barcelona",
            sport= "Basketball",
            event= "Basketball Men's Basketball",
            medal= "Gold"
        )
        evt_obj.save()
        ath_obj = Athlete(
            name="Name",
            sex="M",
            age="25",
            height="123",
            weight="321",
            noc=Comitees.objects.first(),
            event=Event.objects.first()
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

    def test_registration_event(self):
        data = {        
            "team": "Netherlands",
            "games": "1992 Winter",
            "year": 1992,
            "season": "Winter",
            "city": "Albertville",
            "sport": "Speed Skating",
            "event": "Speed Skating Women's 500 metres",
            "medal": "NA"
        }

        response = self.client.post('/api/events/evt/', data)
        self.assertEqual(response.status_code, 201)

    def test_registration_athlete(self):
        data = {        
           "name": "Aleksey Aleksandrovich Abalmasov",
            "sex": "M",
            "age": "28",
            "height": "180",
            "weight": "83",
            "noc": {
                "id": 633,
                "noc": "BLR",
                "region": "Belarus",
                "notes": "['notes']"
            },
            "event": {
                "id": 173,
                "team": "Belarus",
                "games": "2008 Summer",
                "year": 2008,
                "season": "Summer",
                "city": "Beijing",
                "sport": "Canoeing",
                "event": "Canoeing Men's Kayak Fours, 1,000 metres",
                "medal": "Gold"
            }
        
        }

        response = self.client.post('/api/events/ath/', data)
        self.assertEqual(response.status_code, 201)
        
    def test_only_one_comitee(self):
        noc_count = Comitees.objects.count()
        self.assertEqual(noc_count, 1)

    def test_only_one_event(self):
        events_count = Event.objects.count()
        self.assertEqual(events_count, 1)

    def test_only_one_athlete(self):
        athlete_count = Event.objects.count()
        self.assertEqual(athlete_count, 1)

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

    def test_create_event_invalid(self):
        data = {
            "team": "China",
            "games": "1992 Summer",
            "year": "1992",
            "season": "Summer",
            "city": "",
            "sport": "",
            "event": "Basketball Men's Basketball",
            "medal": "NA"
        }
        response = self.client.post('/api/events/evt/', data, format='json')
        self.assertEqual(response.status_code, 400)
    

    def test_create_athlete_invalid(self):
        data = {
            "name": "",
            "sex": "",
            "age": "",
            "height": "180",
            "weight": "83",
            "noc": {
                "noc": "BLR",
                "region": "Belarus",
                "notes": "['notes']"
            },
            "event": {
                "team": "Belarus",
                "games": "2008 Summer",
                "year": 2008,
                "season": "Summer",
                "city": "Beijing",
                "sport": "Canoeing",
                "event": "Canoeing Men's Kayak Fours, 1,000 metres",
                "medal": "Gold"
            }
        }
        response = self.client.post('/api/events/evt/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_evt(self):
        delete_evt = Event.objects.last()
        url = delete_evt.get_api_url()
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
            "team": "China",
            "games": "2012 Summer",
            "year": 2012,
            "season": "Summer",
            "city": "London",
            "sport": "Judo",
            "event": "Judo Men's Extra-Lightweight",
            "medal": "NA"
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

        def test_ath_update(self):
            data = {        
                "id": 173,
                "name": "Aleksey Aleksandrovich Abalmasov",
                "sex": "M",
                "age": "28",
                "height": "180",
                "weight": "83",
                "noc": {
                    "id": 633,
                    "noc": "BLR",
                    "region": "Belarus",
                    "notes": "['notes']"
                },
                "event": {
                    "id": 173,
                    "team": "Belarus",
                    "games": "2008 Summer",
                    "year": 2008,
                    "season": "Summer",
                    "city": "Beijing",
                    "sport": "Canoeing",
                    "event": "Canoeing Men's Kayak Fours, 1,000 metres",
                    "medal": "Gold"
                }
            }
            update_ath = Athlete.objects.last()
            url = update_ath.get_api_url()
            response = self.client.put(url, data , format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_ath_partial_update(self):
            data = {"name":"teste"}
            update_ath = Athlete.objects.first()
            url = update_ath.get_api_url()
            response = self.client.patch(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)