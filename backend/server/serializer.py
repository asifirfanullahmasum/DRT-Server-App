from rest_framework.serializers import ModelSerializer
from .models import *

class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'