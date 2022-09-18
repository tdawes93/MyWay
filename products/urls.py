from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tours, name='tours'),
    path('<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('add/', views.add_tour, name='add_tour'),
]
