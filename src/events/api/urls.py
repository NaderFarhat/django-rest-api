from django.urls import path, include

from .views import EventAPIView, EventRudView, EventFilterView, ComiteeAPIView, ComiteeRudView, ComiteesFilterView

app_name = 'myapi'

urlpatterns = [
    path('evt/', EventAPIView.as_view(), name='event-create'),
    path('evt/list', EventFilterView.as_view(), name='event-filter'),
    path('evt/list/<int:pk>/', EventRudView.as_view(), name='event-rud'),
    path('com/', ComiteeAPIView.as_view(), name='comitee-list'),
    path('com/list', ComiteesFilterView.as_view(), name='comitee-filter'),
    path('com/list/<int:pk>/', ComiteeRudView.as_view(), name='noc-rud'),
]
