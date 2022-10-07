from django.shortcuts import render


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
    template = 'home/footer/destinations.html'
    return render(request, template)


def code_of_conduct(request):
    """
    A view to load the code of conduct page
    """
    template = 'home/footer/code-of-conduct.html'
    return render(request, template)