from django.db import models

# Create your models here.
class Events(models.Model):
    # pk aka id --> numbers
    identification = models.SmallIntegerField()
    name = models.CharField(max_length=255, null=False)
    sex  = models.CharField(max_length=1, null=False)
    age  = models.SmallIntegerField()
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    team   = models.CharField(max_length=40, null=False)
    noc    = models.ForeignKey('Noc', on_delete=models.CASCADE)
    games  = models.CharField(max_length = 40, null=False)
    year   = models.SmallIntegerField(null=False)
    season = models.CharField(max_length = 40, null=False)
    city   = models.CharField(max_length = 40, null=False)
    sport  = models.CharField(max_length = 40, null=False)
    event  = models.CharField(max_length = 40, null=False)
    medal  = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Noc(models.Model):
    noc = models.CharField(max_length=3, null=False)
    region = models.CharField(max_length=30, null=False)
    notes = models.TextField(max_length=255)

    def __str__(self):
        return str(self.noc)