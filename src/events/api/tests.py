import json
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse



class CRUDTestCase(APITestCase):

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
        }

        response = self.client.post('/api/events/teste/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_only_one_noc(self):
        noc_count = Noc.objects.count()
        self.assertEqual(noc_count, 1)

    def test_only_one_athlete(self):
        events_count = Events.objects.count()
        self.assertEqual(events_count, 1)