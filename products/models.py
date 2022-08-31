from django.db import models
from django.core.validators import MaxValueValidator


class Location(models.Model):
    """
    A basic class to represent the list of locations tours can
    be bought for
    """
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        return f'{self.friendly_name}'


class Tour(models.Model):
    """
    A class to represent the products available to purchase
    """
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    itinerary = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    locations = models.ManyToManyField(
        "Location",
        related_name="Location",
    )
    length_of_tour = models.PositiveIntegerField(
        validators=[MaxValueValidator(31)],
        blank=True,
        null=True
    )
    customisable = models.BooleanField(default=True)
    group_discount = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        return f'{self.friendly_name}'
