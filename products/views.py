from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Tour
from .forms import TourForm


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


def add_tour(request):
    """
    Add a tour to the store
    """
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save()
            messages.success(
                request,
                'Tour added to store successfully!'
            )
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            messages.error(
                request,
                'Failed to add tour to store. Please check the form for errors'
            )
    else:
        form = TourForm()
    template = 'products/add_tour.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_tour(request, tour_id):
    """
    Edit a tour in the store
    """
    print(tour_id)
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Tour edited successfully!'
            )
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            messages.error(
                request,
                'Failed to edit the tour. Please check the form for errors'
            )
    else:
        form = TourForm(instance=tour)
    template = 'products/edit_tour.html'
    context = {
        'form': form,
        'tour': tour,
    }
    return render(request, template, context)


def delete_tour(request, tour_id):
    """Delete a tour in the store"""
    tour = get_object_or_404(Tour, pk=tour_id)
    tour.delete()
    messages.success(
        request,
        f'{tour.friendly_name} successfully delete from store')
    return redirect(reverse('tours'))


def site_management(request):
    """Renders navigation to allow superuser to manage site"""
    tours = Tour.objects.all()
    template = 'products/site_management.html'
    context = {
        'tours': tours
    }
    return render(request, template, context)
