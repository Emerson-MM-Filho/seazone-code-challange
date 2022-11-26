from os import urandom
from advertisement.models import Advertisement
from django.db import models


def generate_random_code(cls):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(chars[c % len(chars)] for c in urandom(6))
