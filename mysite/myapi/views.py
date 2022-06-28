from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .serializers import VillianSerializer
from .models import Hero
from .models import Villian


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class VillianViewSet(viewsets.ModelViewSet):
    queryset = Villian.objects.all().order_by('powerlevel')
    serializer_class = VillianSerializer