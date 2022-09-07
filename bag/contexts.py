import decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Tour


def bag_contents(request):

    bag_items = []
    total = 0
    bag = request.session.get('bag', {})
    discount_amount = 0
    increase_guests = 0
    grand_total = 0
    new_total = 0
    old_total = 0

    for tour_date_booked, quantity in bag.items():
        tour_id = tour_date_booked.split()[0]
        date_booked = tour_date_booked.split()[2].split('-')
        day = date_booked[0]
        month = date_booked[1]
        year = date_booked[2]
        tour = get_object_or_404(Tour, pk=tour_id)
        total = quantity * tour.price

        if quantity >= settings.GROUP_DISCOUNT_MIN_NUM:
            old_total = total
            discount_amount = round(total*decimal.Decimal(0.2), 2)
            total = round(total*decimal.Decimal(0.8), 2)
            discount = True
        else:
            increase_guests = settings.GROUP_DISCOUNT_MIN_NUM - quantity
            discount = False

        new_total += total

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
                'total': total,
                'old_total': old_total,
            }
        )

    grand_total += new_total

    context = {
        'bag_items': bag_items,
        'increase_guests': increase_guests,
        'grand_total': grand_total,
        'group_discount_num': settings.GROUP_DISCOUNT_MIN_NUM,
    }

    return context
