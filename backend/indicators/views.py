from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IndicatorSerializer
from .models import Indicator, IndicatorValue


# Create your views here.
class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
