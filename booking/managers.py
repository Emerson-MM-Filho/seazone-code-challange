from typing import Set
from datetime import date
from django.db import models

from propriety.models import Propriety
from challenge.utils import get_date_range_list

class BookingManager(models.Manager):

    def get_unavailable_dates_by_propriety(self, propriety: Propriety) -> Set[date]:
        bookings = self.model.objects.filter(
            advertisement__propriety=propriety
        )
        unavailable_dates = set()
        for booking in bookings:
            unavailable_dates.update(get_date_range_list(booking.check_in, booking.check_out))
        return unavailable_dates
