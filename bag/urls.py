from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:tour_id>/', views.add_to_bag, name='add_to_bag'),
    path('edit/<int:tour_id>/', views.edit_bag, name='edit_bag'),
    path(
        'remove/<int:tour_id>/',
        views.remove_from_bag,
        name='remove_from_bag'
    ),
    path('location/<int:tour_id>', views.add_location, name='add_location'),

]
