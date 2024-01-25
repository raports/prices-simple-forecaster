# serializers for indicators app

from rest_framework import serializers
from .models import Indicator, IndicatorValue


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'