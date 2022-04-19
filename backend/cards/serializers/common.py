from rest_framework import serializers
from ..models import *
from jwt_auth.serializers import UserSerializer

class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = ('__all__')


class PopulatedCardSerializer(CardSerializer):
  created_by = UserSerializer