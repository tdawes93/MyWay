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

    bag = request.session.get('bag', {})

    if tour_id in list(bag.keys()):
        bag[tour_id] += date
    else:
        bag[tour_id] = date

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
