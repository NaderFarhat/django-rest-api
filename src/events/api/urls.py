from django.urls import path, include

from .views import EventAPIView, EventRudView, ComiteeAPIView, ComiteeRudView

app_name = 'myapi'

urlpatterns = [
    path('evt/', EventAPIView.as_view(), name='event-create'),
    path('evt/<int:pk>/', EventRudView.as_view(), name='event-rud'),
    path('com/', ComiteeAPIView.as_view(), name='comitee-list'),
    path('com/<int:pk>/', ComiteeRudView.as_view(), name='noc-rud'),
]
