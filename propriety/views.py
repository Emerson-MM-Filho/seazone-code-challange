from rest_framework import viewsets

from .models import Propriety
from .serializers import ProprietySerializer


class ProprietyViewSet(viewsets.ModelViewSet):
    """
        API endpoint for propriety CRUD.
    """
    queryset = Propriety.objects.all().order_by('-created_at')
    serializer_class = ProprietySerializer
