from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    num_of_guests = 0

    if num_of_guests >= settings.GROUP_DISCOUNT_MIN_NUM:
        grand_total = total*0.8
    else:
        increase_guests = settings.GROUP_DISCOUNT_MIN_NUM - num_of_guests
        grand_total = total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'increase_guests': increase_guests,
        'grand_total': grand_total,
        'group_discount_num': settings.GROUP_DISCOUNT_MIN_NUM,
        'num_of_guests': num_of_guests,
    }

    return context