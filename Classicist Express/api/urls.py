from django.urls import path
from . import views

urlpatterns = [
    path('bd', views.bdaffair, name="bd"),
    path('home', views.home_data, name='home'),
    path('cultural', views.cultural_insights, name='cultural'),
    path('sports', views.sports_insights, name='sports'),
    path('achievements', views.achievements, name='achievements'),
    path('interview', views.interviews, name='interview'),
    path('cc', views.cc, name='cc'),
    path('youth', views.youth, name='youth'),
    path('district', views.district_insights, name='District'),
    path('comics', views.comics, name='Comics'),
    path('trending', views.trending, name='trending'),
    path('diversed', views.diversed, name='diversed')
]
