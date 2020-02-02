from django.db import models

# Create your models here.
class Events(models.Model):
    # pk aka id --> numbers
    identification = models.SmallIntegerField()
    name = models.CharField(max_length=255, null=False)
    sex  = models.CharField(max_length=255, null=False)
    age  = models.CharField(max_length=255, null=True)
    height = models.CharField(max_length=255, null=True)
    weight = models.CharField(max_length=255, null=True)
    team   = models.CharField(max_length=255, null=False)
    noc    = models.ForeignKey('Noc', on_delete=models.CASCADE)
    games  = models.CharField(max_length = 255, null=False)
    year   = models.CharField(max_length = 255, null=False)
    season = models.CharField(max_length = 255)
    city   = models.CharField(max_length = 255, null=False)
    sport  = models.CharField(max_length = 255)
    event  = models.CharField(max_length = 255, null=False)
    medal  = models.CharField(max_length = 255, null=True)

    def __str__(self):
        return self.name
    
    def get_api_url(self, request=None):
        return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)

class Noc(models.Model):
    noc = models.CharField(max_length=255, null=False)
    region = models.CharField(max_length=255, null=False)
    notes = models.TextField(max_length=255)

    def __str__(self):
        return str(self.noc)