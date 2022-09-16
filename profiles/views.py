from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm


def profile(request):
    """
    A view to render the users profile page
    """
    profile_acc = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_acc)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = ProfileForm(instance=profile_acc)
    orders = profile_acc.orders.all()
    template = 'profiles/profile.html'
    context = {
        'profile': profile_acc,
        'form': form,
        'orders': orders
    }

    return render(request, template, context)
