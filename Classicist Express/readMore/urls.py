from django.urls import path
from . import views

urlpatterns = [
    path('', views.readMore_page, name='readmore')
]