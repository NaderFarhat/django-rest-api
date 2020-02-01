from django.urls import path, include

from .views import EventAPIView, EventRudView, EventFilterView, ComiteeAPIView, ComiteeRudView, ComiteesFilterView

app_name = 'myapi'

urlpatterns = [
    #path('evt/', EventAPIView.as_view(), name='event-create'),
    path('evt/', EventFilterView.as_view(), name='event-filter'),
    path('evt/<int:pk>/', EventRudView.as_view(), name='event-detail'),
    #path('com/', ComiteeAPIView.as_view(), name='comitee-list'),
    path('com/', ComiteesFilterView.as_view(), name='comitee-filter'),
    path('com/<int:pk>/', ComiteeRudView.as_view(), name='comitee-detail'),
]
