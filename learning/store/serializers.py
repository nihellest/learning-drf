"""
Store App serializers
"""

from rest_framework import serializers
from .models import Commodity


class CommoditiesSerializer(serializers.ModelSerializer):
    """
    Serializer for store's commodities
    """

    class Meta:
        model = Commodity
        fields = "__all__"
