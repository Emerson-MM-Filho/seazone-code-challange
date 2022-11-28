from rest_framework import viewsets

from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    """
        API endpoint for advertisement CRUD.
    """
    queryset = Advertisement.objects.active().order_by('-created_at')
    serializer_class = AdvertisementSerializer
