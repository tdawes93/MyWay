from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Tour

BAG_SUCCESS = 50


def view_bag(request):
    """
    A view to return the bag and contents
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, tour_id):
    """
    A view to add the date of the specified product to the bag
    """
    tour = Tour.objects.get(pk=tour_id)
    date = request.POST.get('calendar')
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    tour_date_booked = str(tour_id) + ' on ' + date

    bag = request.session.get('bag', {})

    if tour_date_booked in list(bag.keys()):
        bag[tour_date_booked] += quantity
    else:
        bag[tour_date_booked] = quantity
        messages.add_message(
            request,
            BAG_SUCCESS,
            f'Added { tour.friendly_name } to your bag!'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, tour_id):
    """
    A view to add the date of the specified product to the bag
    """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    bag_item_id = request.POST.get('bag_item_id')
    tour_date_booked = ' '.join(bag_item_id.split('_'))

    for tour_date_booked in list(bag.keys()):
        if quantity > 0:
            bag[tour_date_booked] = quantity
        else:
            bag.pop(tour_date_booked)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, tour_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag_item_id = request.POST.get('bag_item_id')
        tour_date_booked = ' '.join(bag_item_id.split('_'))
        bag.pop(tour_date_booked)
        request.session['bag'] = bag

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
