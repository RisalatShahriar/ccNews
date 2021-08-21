from django.urls import path
from . import views

urlpatterns = [
    path('', views.publish_page, name='publish')
]
