import json
import time

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from profiles.models import Profile
from products.models import Tour
from .models import Order, OrderItem


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'contact_number': settings.DEFAULT_CONTACT_NUMBER,
                }
        )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [customer_email])

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # cleans data in billing details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = Profile.objects.get(
                user__username=username
                )
            if save_info == 'save':
                profile.default_phone_number = billing_details.phone
                profile.default_country = billing_details.address.country
                profile.default_town_or_city = billing_details.address.city
                profile.default_street_address1 = billing_details.address.line1
                profile.default_street_address2 = billing_details.address.line2
                profile.default_county = billing_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 10:
            try:
                order = Order.objects.get(
                    name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]}'
                    f' | SUCCESS: Verified order already in database'),
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    profile=profile,
                    name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for tour_date_booked, quantity in json.loads(bag).items():
                    tour_id = tour_date_booked.split()[0]
                    tour = get_object_or_404(Tour, pk=tour_id)
                    date_booked = ' '.join(
                        tour_date_booked.split()[2].split('-')
                        )
                    order_item = OrderItem(
                        order=order,
                        tour=tour,
                        number_of_guests=quantity,
                        date_of_trip_or_event=date_booked,
                    )
                    order_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=(
                        f'Webhook received: {event["type"]}'
                        f' | ERROR: {e}'),
                    status=500
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]}'
                f' | SUCCESS: Created order in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
