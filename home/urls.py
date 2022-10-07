from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about_us/', views.about_us, name='about_us'),
    path('destinations/', views.destinations, name='destinations'),
    path('code_of_conduct/', views.code_of_conduct, name='code_of_conduct'),
    path('faq/', views.faq, name='faq'),
]
