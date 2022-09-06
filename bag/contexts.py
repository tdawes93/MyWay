from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Tour


def bag_contents(request):

    bag_items = []
    total = 0
    num_of_guests = 0
    bag = request.session.get('bag', {})

    for tour_date_booked, quantity in bag.items():
        tour_id = tour_date_booked.split()[0]
        date_booked = tour_date_booked.split()[2]
        tour = get_object_or_404(Tour, pk=tour_id)
        total = quantity * tour.price
        num_of_guests += quantity
        bag_items.append(
            {
                'tour_id': tour_id,
                'date_booked': date_booked,
                'quantity': quantity,
                'tour': tour,
            }
        )

    if num_of_guests >= settings.GROUP_DISCOUNT_MIN_NUM:
        grand_total = total*0.8
    else:
        increase_guests = settings.GROUP_DISCOUNT_MIN_NUM - num_of_guests
        grand_total = total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'increase_guests': increase_guests,
        'grand_total': grand_total,
        'group_discount_num': settings.GROUP_DISCOUNT_MIN_NUM,
        'num_of_guests': num_of_guests,
    }

    return context