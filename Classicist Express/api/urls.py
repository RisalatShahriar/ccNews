from django.urls import path
from . import views

urlpatterns = [
    path('bd', views.bdaffair, name="bd_api"),
    path('home', views.home_data, name='home_api'),
    path('cultural', views.cultural_insights, name='cultural_api'),
    path('sports', views.sports_insights, name='sports_api'),
    path('international', views.internatioal, name='achievements_api'),
    path('interview', views.interviews, name='interview_api'),
    path('cc', views.cc, name='cc_api'),
    path('youth', views.youth, name='youth_api'),
    path('district', views.district_insights, name='district_api'),
    path('comics', views.comics, name='comics_api'),
    path('trending', views.trending, name='trending_api'),
    path('diversed', views.diversed, name='diversed_api')
]
