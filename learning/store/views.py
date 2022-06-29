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
    serializer_class = CommoditiesSerializer

    def get_queryset(self):
        queryset = Commodity.objects.all()
        if 'all' in self.request.query_params:
            return Commodity.objects.all()
        return Commodity.objects.filter(is_active=True)