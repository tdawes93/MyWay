from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Tour


def bag_contents(request):

    bag_items = []
    total = 0
    bag = request.session.get('bag', {})

    for tour_date_booked, quantity in bag.items():
        tour_id = tour_date_booked.split()[0]
        date_booked = tour_date_booked.split()[2].split('-')
        day = date_booked[0]
        month = date_booked[1]
        year = date_booked[2]
        tour = get_object_or_404(Tour, pk=tour_id)
        total = quantity * tour.price

        if quantity >= settings.GROUP_DISCOUNT_MIN_NUM:
            grand_total = total*0.8
            discount = True
            discount_amount = total*0.2
        else:
            increase_guests = settings.GROUP_DISCOUNT_MIN_NUM - quantity
            grand_total = total
            discount = False

        bag_items.append(
            {
                'tour_id': tour_id,
                'date_booked': date_booked,
                'day': day,
                'month': month,
                'year': year,
                'quantity': quantity,
                'tour': tour,
                'discount': discount,
                'discount_amount': discount_amount,
                'total': total
            }
        )

    context = {
        'bag_items': bag_items,
        'increase_guests': increase_guests,
        'grand_total': grand_total,
        'group_discount_num': settings.GROUP_DISCOUNT_MIN_NUM,
    }

    return context
