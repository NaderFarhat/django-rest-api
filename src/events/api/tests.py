import json
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from events.models import Event, Comitees



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
        
    def test_only_one_noc(self):
        noc_count = Comitees.objects.count()
        self.assertEqual(noc_count, 1)

    def test_only_one_athlete(self):
        events_count = Event.objects.count()
        self.assertEqual(events_count, 1)