from django.shortcuts import render
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
