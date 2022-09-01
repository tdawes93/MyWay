from django.shortcuts import render,  get_object_or_404
from .models import Tour


def all_tours(request):
    """
    View to display the list of tours available
    """
    tours = Tour.objects.all().order_by('friendly_name')

    sort = None
    direction = None

# Taken from CI Boutique-Ado
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tours = tours.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tours = tours.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'tours': tours,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/tours.html', context)


def tour_detail(request, tour_id):
    """
    View to display individual tour information
    """
    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'products/tour_detail.html', context)
