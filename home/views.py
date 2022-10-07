from django.shortcuts import render

from products.models import Location


def home(request):
    """
    A view to return the homepage
    """
    return render(request, 'home/index.html')


def about_us(request):
    """
    A view to load the about us page
    """
    template = 'home/footer/about-us.html'
    return render(request, template)


def destinations(request):
    """
    A view to load the destinations page
    """
    locations = Location.objects.all()
    template = 'home/footer/destinations.html'
    context = {
        'locations': locations,
    }
    return render(request, template, context)


def code_of_conduct(request):
    """
    A view to load the code of conduct page
    """
    template = 'home/footer/code-of-conduct.html'
    return render(request, template)


def faq(request):
    """
    A view to load the FAQ page
    """
    template = 'home/footer/faq.html'
    return render(request, template)
