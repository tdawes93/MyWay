from django.shortcuts import render


def view_bag(request):
    """
    A view to return the bag and contents
    """
    return render(request, 'bag/bag.html')
