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
    path('diversed', views.diversed, name='diversed_api'),
    path('bd/top', views.bdaffair_top, name="top_bd_api"),
    path('home/top', views.home_data_top, name='top_home_api'),
    path('cultural/top', views.cultural_insights_top, name='top_cultural_api'),
    path('sports/top', views.sports_insights_top, name='top_sports_api'),
    path('international/top', views.internatioal_top, name='top_achievements_api'),
    path('interview/top', views.interviews_top, name='top_interview_api'),
    path('cc/top', views.cc_top, name='top_cc_api'),
    path('youth/top', views.youth_top, name='top_youth_api'),
    path('district/top', views.district_insights_top, name='top_district_api'),
    path('comics/top', views.comics_top, name='top_comics_api'),
    path('trending/top', views.trending_top, name='top_trending_api'),
    path('diversed/top', views.diversed_top, name='top_diversed_api')
]