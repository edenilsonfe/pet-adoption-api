from rest_framework import serializers
from pets.models import Pet


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        exclude = ('created', )
