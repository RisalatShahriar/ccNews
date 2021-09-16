from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_page, name='registration'),
    path('temp/<str:id>', views.temp_registration_page, name='temp_registration')
]