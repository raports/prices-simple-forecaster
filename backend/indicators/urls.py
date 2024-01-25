#urls for indicator views

from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'indicators', views.IndicatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]