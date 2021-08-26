from django.urls import path
from . import views

urlpatterns = [
    path('<str:link>', views.readMore_page, name='readmore')
]
