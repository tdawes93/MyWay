from django.shortcuts import render,  get_object_or_404
from .models import Tour


def all_tours(request):
    """
    View to display the list of tours available
    """
    tours = Tour.objects.all().order_by('friendly_name')

    context = {
        'tours': tours,
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
