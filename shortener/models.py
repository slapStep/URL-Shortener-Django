from builtins import map

from django.db import models


# Create your models here.
class Shortener(models.Model):
    """
    Creates a short url based on the long one

    created -> Date when the short url was created

    times_followed -> Times the shortened link has been followed

    long_url -> The original link

    short_url -> New shortened url
    """

    created = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)

    long_url = models.URLField()

    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

