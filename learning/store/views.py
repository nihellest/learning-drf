"""
Store App URLs
"""

from rest_framework import viewsets
from .models import Commodity
from .serializers import CommoditiesSerializer


class CommoditiesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for store's commodities
    """
    queryset = Commodity.objects.all()
    serializer_class = CommoditiesSerializer
