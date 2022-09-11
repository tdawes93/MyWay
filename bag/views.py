from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
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
    tour = get_object_or_404(Tour, pk=tour_id)
    date = request.POST.get('calendar')
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    tour_date_booked = str(tour_id) + ' on ' + date
    day = date.split('-')[0]
    month = date.split('-')[1].capitalize()
    year = date.split('-')[2]

    bag = request.session.get('bag', {})

    if tour_date_booked in list(bag.keys()):
        bag[tour_date_booked] += quantity
        messages.add_message(
            request,
            BAG_SUCCESS,
            f'Updated the number of travellers in your bag for { tour.friendly_name } on {day} {month} {year}'
        )
    else:
        bag[tour_date_booked] = quantity
        messages.add_message(
            request,
            BAG_SUCCESS,
            f'{ tour.friendly_name } on {day} {month} {year} added to your bag!'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, tour_id):
    """
    A view to add the date of the specified product to the bag
    """
    tour = get_object_or_404(Tour, pk=tour_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    bag_item_id = request.POST.get('bag_item_id')
    tour_date_booked = ' '.join(bag_item_id.split('_'))
    date = tour_date_booked.split()[2]
    day = date.split('-')[0]
    month = date.split('-')[1].capitalize()
    year = date.split('-')[2]

    if quantity > 0:
        bag[tour_date_booked] = quantity
        messages.add_message(
            request,
            BAG_SUCCESS,
            f'Updated the number of travellers in your bag for { tour.friendly_name } on {day} {month} {year}'
        )
    else:
        bag.pop(tour_date_booked)
        messages.add_message(
            request,
            BAG_SUCCESS,
            f'Removed { tour.friendly_name } on {day} {month} {year} from your bag!'
        )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, tour_id):
    """Remove the item from the shopping bag"""
    tour = get_object_or_404(Tour, pk=tour_id)
    try:
        bag = request.session.get('bag', {})
        bag_item_id = request.POST.get('bag_item_id')
        tour_date_booked = ' '.join(bag_item_id.split('_'))
        date = tour_date_booked.split()[2]
        day = date.split('-')[0]
        month = date.split('-')[1].capitalize()
        year = date.split('-')[2]
        bag.pop(tour_date_booked)
        messages.add_message(
            request,
            BAG_SUCCESS,
            f'Removed { tour.friendly_name } on {day} {month} {year} from your bag!'
        )
        request.session['bag'] = bag

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error receiving item: {e}')
        return HttpResponse(status=500)
