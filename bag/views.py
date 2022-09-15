from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages
from django.conf import settings
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
        for item in bag:
            if bag[tour_date_booked] + quantity >= tour.max_num_of_guests:
                messages.error(
                    request, (
                        f'Cannot add {quantity} traveller(s) for '
                        f'{tour.friendly_name} on {day} {month} {year}'
                        f'to your bag as it will exceed the '
                        f'maximum group size of {tour.max_num_of_guests}. '
                        f'Please change the number of guests to add your tour.'
                    ))
                return HttpResponse(status=400)
            else:
                bag[tour_date_booked] += quantity
                messages.add_message(
                    request,
                    BAG_SUCCESS, (
                        f'Updated the number of travellers in your bag '
                        f'for {tour.friendly_name} on {day} {month} {year}'
                    )
                )
                if tour.group_discount:
                    if bag[tour_date_booked] >= settings.GROUP_DISCOUNT_MIN_NUM:
                        messages.success(
                            request, (
                                'Congratulations you have qualified for '
                                'a group discount of 20% off!'
                            )
                        )
    else:
        bag[tour_date_booked] = quantity
        messages.add_message(
            request,
            BAG_SUCCESS,
            f'{tour.friendly_name} on {day} {month} {year} added to your bag!'
        )
        if tour.group_discount:
            if bag[tour_date_booked] >= settings.GROUP_DISCOUNT_MIN_NUM:
                messages.success(
                    request, (
                        'Congratulations you have qualified for '
                        'a group discount of 20% off!'
                    )
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
            BAG_SUCCESS, (
                f'Updated the number of travellers in your bag '
                f'for {tour.friendly_name} on {day} {month} {year}'
            )
        )
        if tour.group_discount:
            if bag[tour_date_booked] >= settings.GROUP_DISCOUNT_MIN_NUM:
                messages.success(
                    request, (
                        'Congratulations you have qualified '
                        'for a group discount of 20% off!'
                    )
                )
    else:
        bag.pop(tour_date_booked)
        messages.add_message(
            request,
            BAG_SUCCESS, (
                f'Removed {tour.friendly_name} on '
                f'{day} {month} {year} from your bag!'
            )
        )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def add_location(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    bag = request.session.get('location', {})
    bag_item_id = request.POST.get('bag_item_id')
    tour_date_booked = ' '.join(bag_item_id.split('_'))
    date = tour_date_booked.split()[2]
    day = date.split('-')[0]
    month = date.split('-')[1].capitalize()
    year = date.split('-')[2]

    location = request.POST.get('location')

    if location:
        location_friendly_name = (' '.join(location.split('_')).title())
        bag[tour_date_booked] = location_friendly_name
        messages.add_message(
            request,
            BAG_SUCCESS, (
                f'{location_friendly_name} added to '
                f'{tour.friendly_name} on {day} {month} {year}!'
            )
        )
    else:
        locations = []
        for place in tour.locations.all():
            if request.POST.get(f'{place}'):
                location = request.POST.get(f'{place}')
                location_friendly_name = (
                    ' '.join(location.split('_')).title()
                )
                locations.append(location_friendly_name)
        bag[tour_date_booked] = locations
        places = ', '.join(locations)
        messages.add_message(
            request,
            BAG_SUCCESS,
            f'{places} added to {tour.friendly_name} on {day} {month} {year}!'
        )

    request.session['location'] = bag
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
            BAG_SUCCESS,(
                f'Removed {tour.friendly_name} on '
                f'{day} {month} {year} from your bag!'
            )
        )
        request.session['bag'] = bag

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error receiving item: {e}')
        return HttpResponse(status=500)
