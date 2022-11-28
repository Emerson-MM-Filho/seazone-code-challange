from rest_framework import viewsets

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
        API endpoint for booking CRUD.
    """
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer
    http_method_names = [
        "get",
        "post",
        "delete",
        "head",
        "options",
        "trace",
    ]
