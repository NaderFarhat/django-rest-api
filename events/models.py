from django.db import models

from rest_framework.reverse import reverse

class Comitees(models.Model):
    noc     = models.CharField(max_length=255, null=False)
    region  = models.CharField(max_length=255, null=False)
    notes   = models.CharField(max_length=100, blank=True, null=True, default='')

    def __str__(self):
        return self.noc

    def get_api_url(self, request=None):
        return reverse("api-events:comitee-detail", kwargs={'pk': self.pk}, request=request)


class Event(models.Model):
    
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=25)
    year = models.IntegerField()
    season = models.CharField(max_length=25)
    city = models.CharField(max_length=20)
    sport = models.CharField(max_length=35)
    event = models.CharField(max_length=80)
    medal = models.CharField(max_length=10)


    def __str__(self):
        return self.games
        
    def get_api_url(self, request=None):
        return reverse("api-events:event-detail", kwargs={'pk': self.pk}, request=request)


class Athlete(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=2)
    age = models.CharField(max_length=4)
    height = models.CharField(max_length=6)
    weight = models.CharField(max_length=6)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    noc = models.ForeignKey(Comitees, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def get_api_url(self, request=None):
        return reverse("api-events:athlete-detail", kwargs={'pk': self.pk}, request=request)





