import json
import stripe

from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings


from bag.contexts import bag_contents
from products.models import Tour
from profiles.forms import ProfileForm
from profiles.models import Profile
from .forms import OrderForm
from .models import Order, OrderItem


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            'bag': json.dumps(request.session.get('bag', {}))
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, (
            'Sorry your payment cannot '
            'be processed right now. '
            'Please try again later.')
            )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    A view to show a summary of the bag and handle payment methods
    and the order forms
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            print(f'stripe_pid = {order.stripe_pid}')
            order.original_bag = json.dumps(bag)
            print(f'og bag = {order.original_bag}')
            order.save()
            print(f'ptotal = {order.product_total}')
            print(f'gtotal = {order.grand_total}')
            for tour_date_booked, quantity in bag.items():
                try:
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
                except Tour.DoesNotExist:
                    messages.error(request, (
                        "A tour in your bag does not exist in our database. "
                        "Please call us and we'll create a tour for you!"
                        )
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            print(f'ptotal2 = {order.product_total}')
            print(f'gtotal2 = {order.grand_total}')

            request.session['save_info'] = request.POST.get('save-info')
            return redirect(reverse(
                'checkout_success',
                args=[order.order_number]
                )
            )
        else:
            messages.error(request, (
                'There was an error with your form'
                'Please check your information'
                )
            )
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag")
            return redirect(reverse('tours'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='cad',
            )

        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,

                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    A view to handle the successful checkouts after payment
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.profile = profile
        order.save()

        # Save the user's info
        if save_info == 'save':
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }

            profile_form = ProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()

    messages.success(request, (
        f'Order successful! '
        f'Your booking number is {order_number}. '
        f'You will receive a confirmation email to {order.email}. '
        f'If you do not receive this email please check your junk folder')
    )

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
