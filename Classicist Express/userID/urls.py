from django.urls import path
from . import views

urlpatterns = [
    path('<str:ID>', views.userID_home, name='userID')
]
