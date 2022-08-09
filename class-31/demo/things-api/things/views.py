from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

from .models import Thing
from .serializers import ThingSerializer
# Create your views here.

class ThingListView(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class ThingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

