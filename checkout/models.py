import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Tour
from profiles.models import Profile


class Order(models.Model):
    """
    A model to create the individual order purchases
    """
    order_number = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        editable=False
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders'
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(
        max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    product_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    total_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    def _generate_order_number(self):
        """Generate a random unique order number"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for group discounts.
        """
        self.product_total = self.orderitems.aggregate(
            Sum('tour_total'))['tour_total__sum'] or 0
        self.total_discount = self.orderitems.aggregate(
            Sum('tour_discount'))['tour_discount__sum']
        print(self.product_total)
        print(type(self.product_total))
        self.grand_total = self.product_total - self.total_discount
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """
    A model class to represent each individual item in the order
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='orderitems'
    )
    tour = models.ForeignKey(
        Tour,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    number_of_guests = models.IntegerField(null=False, blank=False, default=0)
    date_of_trip_or_event = models.CharField(max_length=100)
    tour_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        default=0,
    )
    tour_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False,
        default=0,
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total and calculate group discounts
        for each item in the order.
        """
        self.tour_total = self.tour.price*self.number_of_guests
        if self.tour.group_discount:
            if self.number_of_guests >= settings.GROUP_DISCOUNT_MIN_NUM:
                self.tour_discount = round(Decimal(float(self.tour_total) * 0.2), 2)
        else:
            self.tour_discount = 0
        print(self.tour_discount)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.tour.name} on order {self.order.order_number}'
