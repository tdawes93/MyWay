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


class Date(models.Model):
    """
    A class to represent the months available to purchase tour
    """
    # Specifiy choices for dropdown option
    JAN = 'Jan'
    FEB = 'Feb'
    MAR = 'Mar'
    APR = 'Apr'
    MAY = 'May'
    JUN = 'Jun'
    JUL = 'Jul'
    AUG = 'Aug'
    SEP = 'Sep'
    OCT = 'Oct'
    NOV = 'Nov'
    DEC = 'Dec'
    MONTH_CHOICES = [
        (JAN, 'Jan'),
        (FEB, 'Feb'),
        (MAR, 'Mar'),
        (APR, 'Apr'),
        (MAY, 'May'),
        (JUN, 'Jun'),
        (JUL, 'Jul'),
        (AUG, 'Aug'),
        (SEP, 'Sep'),
        (OCT, 'Oct'),
        (NOV, 'Nov'),
        (DEC, 'Dec'),
    ]
    name = models.CharField(
        max_length=30,
        choices=MONTH_CHOICES,
        default=0,
    )

    def __str__(self):
        return f'{self.name}'


class Tour(models.Model):
    """
    A class to represent the products available to purchase
    """
    # Specifiy choices for dropdown option
    BUS = 'Bus'
    FERRY = 'Ferry'
    TRAIN = 'Train'
    BUS_AND_FERRY = 'Bus and Ferry'
    BUS_AND_TRAIN = 'Bus and Train'
    TRAIN_AND_FERRY = 'Train and Ferry'
    TRANSPORT_CHOICES = [
        (BUS, 'Bus'),
        (FERRY, 'Ferry'),
        (TRAIN, 'Train'),
        (BUS_AND_FERRY, 'Bus and Ferry'),
        (BUS_AND_TRAIN, 'Bus and Train'),
        (TRAIN_AND_FERRY, 'Train and Ferry'),
    ]
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
    accomodation = models.PositiveIntegerField(
        validators=[MaxValueValidator(31)],
        blank=True,
        null=True
    )
    num_of_dinner = models.PositiveIntegerField(
        validators=[MaxValueValidator(31)],
        blank=True,
        null=True
    )
    num_of_breakfast = models.PositiveIntegerField(
        validators=[MaxValueValidator(31)],
        blank=True,
        null=True
    )
    transport = models.CharField(
        max_length=30,
        choices=TRANSPORT_CHOICES,
        default=0,
    )
    max_num_of_guests = models.PositiveIntegerField(
        validators=[MaxValueValidator(20)],
        default=10,
    )
    customisable = models.BooleanField(default=True)
    group_discount = models.BooleanField(default=True)
    dates = models.ManyToManyField(
        "Date",
        related_name="Date"
    )
    choose_location = models.BooleanField(null=True, blank=True)
    choose_multiple_locations = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        return f'{self.friendly_name}'
