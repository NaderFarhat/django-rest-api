from django.urls import path, include

from .views import (
    ApiRootView,
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
    path('list/', ApiRootView.as_view(), name='api-root'),
    path('game/', GameAPIView.as_view(), name='game-list'),
    path('game/<int:pk>/', GameRudView.as_view(), name='game-detail'),
    path('evt/', EventAPIView.as_view(), name='event-list'),
    path('evt/<int:pk>/', EventRudView.as_view(), name='event-detail'),
    path('ath/', AthleteAPIView.as_view(), name='athlete-list'),
    path('ath/<int:pk>/', AthleteRudView.as_view(), name='athlete-detail'),
    path('com/', ComiteeAPIView.as_view(), name='com-list'),
    path('com/<int:pk>/', ComiteeRudView.as_view(), name='co-detail'),
]
