from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bd', views.bdaffair_page, name="bd"),
    path('home', views.home_data_page, name='home'),
    path('cultural', views.cultural_insights_page, name='cultural'),
    path('sports', views.sports_insights_page, name='sports'),
    path('international', views.internatioal_page, name='achievements'),
    path('interview', views.interviews_page, name='interview'),
    path('cc', views.cc_page, name='cc'),
    path('youth', views.youth_page, name='youth'),
    path('district', views.district_insights_page, name='District'),
    path('comics', views.comics_page, name='Comics'),
    path('trending', views.trending_page, name='trending'),
    path('diversed', views.diversed_page, name='diversed')
]
