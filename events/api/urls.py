from django.urls import path, include

from .views import EventRudView, EventAPIView, EventFilterView, NocFilterView, NocRudView, NocAPIView

app_name = 'myapi'

urlpatterns = [
    path('athletes/', EventFilterView.as_view(), name='event-list'),
    #path('athletes/<int:pk>/', EventView.as_view(), name='event-detail'),
    path('teste/<int:pk>/', EventRudView.as_view(), name='post-rud'),
    path('teste/', EventAPIView.as_view(), name='post-create'),
    path('nocs/', NocFilterView.as_view(), name='noc-list'),
    path('nocs/<int:pk>/', NocRudView.as_view(), name='noc-rud'),
    path('nocs/', NocAPIView.as_view(), name='noc-create')
]

