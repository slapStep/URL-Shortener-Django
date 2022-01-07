"""
Utility functions for shortener
"""

from django.conf import settings

from random import choice

from string import ascii_lowercase, digits

SIZE = getattr(settings, 'MAXIMUM_URL_CHARS', 7)

ALL_CHARS = ascii_lowercase + digits


def create_random_string(chars=ALL_CHARS):
    """
    Creates random string of digits and lowercase ascii characters with fixed length
    """
    return ''.join([choice(chars) for _ in range(SIZE)])


def create_shortened_url(model_instance):
    """
    Creates unique shortened url
    """
    random_string = create_random_string()

    # Getting model class (Shortener)
    model_class = model_instance.__class__

    # Checking if new url string already exists
    if model_class.objects.filter(short_url=random_string).exists():
        return create_shortened_url(model_instance)

    return random_string


