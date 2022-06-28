# serializers.py

from rest_framework import serializers
from .models import Hero
from .models import Villian


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')


class VillianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villian
        fields = ('id', 'name', 'powerlevel')