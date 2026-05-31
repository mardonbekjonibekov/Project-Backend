from rest_framework import generics

from .models import Event
from .serializers import EventSerializer


class EventListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(is_active=True)


class EventDetailAPIView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(is_active=True)
