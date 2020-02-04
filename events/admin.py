from django.contrib import admin
from events.models import Event, Comitees, Athlete, Game

admin.site.register(Event)
admin.site.register(Comitees)
admin.site.register(Athlete)
admin.site.register(Game)