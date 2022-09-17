import decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Tour

from datetime import date


def bag_contents(request):

    bag_items = []
    location_items = []
    total = 0
    discount_amount = 0
    increase_guests = 0
    grand_total = 0
    new_total = 0
    old_total = 0
    discount = False
    product_count = 0
    total_discount = 0
    bag = request.session.get('bag', {})
    location = request.session.get('location', {})

    for tour_date_booked, quantity in bag.items():
        bag_item_id = '_'.join(tour_date_booked.split())
        tour_id = tour_date_booked.split()[0]
        date_booked = tour_date_booked.split()[2].split('-')
        day = date_booked[0]
        month = date_booked[1]
        year = date_booked[2]
        tour = get_object_or_404(Tour, pk=tour_id)
        total = quantity * tour.price

        if tour.group_discount:
            if quantity >= settings.GROUP_DISCOUNT_MIN_NUM:
                old_total = total
                discount_amount = round(total*decimal.Decimal(0.2), 2)
                total = round(total*decimal.Decimal(0.8), 2)
                discount = True
                total_discount += discount_amount

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
                'bag_item_id': bag_item_id,
            }
        )

    for tour_date_booked, location in location.items():
        bag_item_id = '_'.join(tour_date_booked.split())

        location_items.append(
            {
                'location': location,
                'bag_item_id': bag_item_id
            }
        )

    product_count = len(bag)
    grand_total += new_total
    pre_discount_total = grand_total + total_discount

    context = {
        'bag_items': bag_items,
        'location_items': location_items,
        'increase_guests': increase_guests,
        'grand_total': grand_total,
        'group_discount_num': settings.GROUP_DISCOUNT_MIN_NUM,
        'product_count': product_count,
        'total_discount': total_discount,
        'pre_discount_total': pre_discount_total,
        'todays_date': date.today()
    }

    return context
