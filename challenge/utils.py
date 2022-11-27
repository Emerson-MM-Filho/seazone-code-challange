from os import urandom
from datetime import date, timedelta
from typing import Set

def generate_random_code(length: int) -> str:
    """Generate a random code with the given length"""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(chars[c % len(chars)] for c in urandom(length))

def get_date_range_list(start_date: date, end_date: date) -> Set[date]:
    """Return list of datetime.date objects between start_date and end_date (inclusive)"""
    date_set = set()
    curr_date = start_date
    while curr_date <= end_date:
        date_set.add(curr_date)
        curr_date += timedelta(days=1)
    return date_set