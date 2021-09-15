from django.urls import path
from . import views

urlpatterns = [
    path('<str:link>', views.readMore_page, name='readmore'),
    path('approve/<str:link>', views.readmore_approve)
]
