from django.shortcuts import render, redirect


def view_bag(request):
    """
    A view to return the bag and contents
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, tour_id):
    """
    A view to add the date of the specified product to the bag
    """
    date = request.POST.get('calendar')
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    tour_date_booked = str(tour_id) + ' on ' + date

    bag = request.session.get('bag', {})

    if tour_date_booked in list(bag.keys()):
        bag[tour_date_booked] += quantity
    else:
        bag[tour_date_booked] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
