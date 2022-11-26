from os import urandom

def generate_random_code(length: int) -> str:
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(chars[c % len(chars)] for c in urandom(length))
