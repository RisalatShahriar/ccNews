from django.urls import path
from . import views

urlpatterns = [
    path('bd', views.bdaffair, name="bd")
]
