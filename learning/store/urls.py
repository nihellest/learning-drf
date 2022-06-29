"""
Store App URLs
"""

from django.urls import path
from rest_framework import routers
from .views import CommoditiesViewSet

router = routers.DefaultRouter()
router.register(
    r'commodities',
    CommoditiesViewSet,
    basename='commodity'
)

urlpatterns = router.urls