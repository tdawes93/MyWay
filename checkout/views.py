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
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
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

            request.session['save_info'] = 'save_info' in request.POST
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
    messages.success(request, (
        f'Order successful!'
        f'Your booking number is {order_number}'
        f'You will receive a confirmation email to {order.email}'
        f'If you do not receive this email please check your junk folder')
    )

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
