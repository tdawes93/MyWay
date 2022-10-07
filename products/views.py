from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Tour, Location
from .forms import TourForm, LocationForm


def all_tours(request):
    """
    View to display the list of tours available
    """
    tours = Tour.objects.all().order_by('friendly_name')

    sort = None
    direction = None
    search = None

    # Taken from CI Boutique-Ado
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter anything in the search. Please try again"
                    )
                return redirect(reverse('tours'))

            search = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(itinerary__icontains=query)
                | Q(price__icontains=query)
                | Q(length_of_tour__icontains=query)
            )
            tours = tours.filter(search)

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
        'search_term': search,
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


@login_required
@user_passes_test(lambda u: u.is_superuser)
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


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_tour(request, tour_id):
    """
    Edit a tour in the store
    """
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


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_tour(request, tour_id):
    """Delete a tour in the store"""
    tour = get_object_or_404(Tour, pk=tour_id)
    tour.delete()
    messages.success(
        request,
        f'{tour.friendly_name} successfully deleted from store')
    return redirect(reverse('tours'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_location(request):
    """
    Add a location to the store
    """
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Location added to store successfully!'
            )
            return redirect(reverse('homepage'))
        else:
            messages.error(
                request,
                'Failed to add location to store. Please check for errors'
            )
    else:
        form = LocationForm()
    template = 'products/add_location.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_location(request, location_id):
    """
    Edit a location in the store
    """
    location = get_object_or_404(Location, pk=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Location edited successfully!'
            )
            return redirect(reverse('homepage'))
        else:
            messages.error(
                request,
                'Failed to edit the location. Please check for errors'
            )
    else:
        form = LocationForm(instance=location)
    template = 'products/edit_location.html'
    context = {
        'form': form,
        'location': location,
    }
    return render(request, template, context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_location(request, location_id):
    """Delete a location in the store"""
    location = get_object_or_404(Location, pk=location_id)
    location.delete()
    messages.success(
        request,
        f'{location.friendly_name} successfully deleted from store')
    return redirect(reverse('homepage'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def site_management(request):
    """Renders navigation to allow superuser to manage site"""
    tours = Tour.objects.all()
    locations = Location.objects.all()
    template = 'products/site_management.html'
    context = {
        'tours': tours,
        'locations': locations,
    }
    return render(request, template, context)
