import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Tour


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
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    product_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    total_discount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=6,
        decimal_places=6,
        null=False,
        default=0
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
            Sum('tour_total'))['tour_total__sum']
        self.total_discount = self.orderitems.aggregate(
            Sum('tour_discount'))['tour_discount__sum']
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
    date_of_trip_or_event = models.DateField(auto_now=False)
    tour_discount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
    )
    tour_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total and calculate group discounts
        for each item in the order.
        """
        self.tour_total = self.tour.price * self.number_of_guests
        if self.number_of_guests >= settings.GROUP_DISCOUNT_MIN_NUM:
            self.tour_discount = self.tour_total*0.2
        else:
            self.tour_discount = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.tour.name} on order {self.order.order_number}'
