from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import date, datetime

from checkout.models import Order

from .models import Profile
from .forms import ProfileForm


@login_required
def profile(request):
    """
    A view to render the users profile page
    """
    profile_acc = get_object_or_404(Profile, user=request.user)
    date_booked_id = ''

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_acc)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Profile update failed. Please check the form for errors'
            )
    else:
        form = ProfileForm(instance=profile_acc)
    orders = profile_acc.orders.all()
    template = 'profiles/profile.html'

    for order in orders:
        orderitems = order.orderitems.all()
        for item in orderitems:
            date_notime = '/'.join(item.date_of_trip_or_event.split())
            date_withtime = date_notime
            date_booked_id = datetime.strptime(date_withtime, '%d/%b/%Y').date()

    context = {
        'profile': profile_acc,
        'form': form,
        'orders': orders,
        'date_booked_id': date_booked_id
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
