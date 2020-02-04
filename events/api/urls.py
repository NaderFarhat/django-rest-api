from django.urls import path, include

from .views import (
    EventAPIView,
    EventRudView,
    ComiteeAPIView,
    ComiteeRudView,
    AthleteAPIView,
    AthleteRudView,
    GameAPIView,
    GameRudView
)

app_name = 'myapi'

urlpatterns = [
    path('game/', GameAPIView.as_view(), name='event-list'),
    path('game/<int:pk>/', GameRudView.as_view(), name='event-detail'),
    path('evt/', EventAPIView.as_view(), name='event-list'),
    path('evt/<int:pk>/', EventRudView.as_view(), name='event-detail'),
    path('ath/', AthleteAPIView.as_view(), name='comitee-list'),
    path('ath/<int:pk>/', AthleteRudView.as_view(), name='comitee-detail'),
    path('com/', ComiteeAPIView.as_view(), name='comitee-list'),
    path('com/<int:pk>/', ComiteeRudView.as_view(), name='comitee-detail'),
]
