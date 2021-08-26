from django.http import HttpResponse
from publish import models
from . import helper
import json


# Create your views here.
def home_data(req):
    return HttpResponse(helper.api_send(models.News.objects.all()))

def bdaffair(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Bangladesh Affairs')))

def cultural_insights(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Cultural Insights')))

def sports_insights(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Sports Insight')))

def internatioal(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='International Affairs')))

def interviews(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Small Talk With Gems')))

def cc(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Cultural Classicists')))

def youth(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Youth')))

def district_insights(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='District Insights')))

def comics(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Comics')))

def trending(req):
    return HttpResponse(helper(models.News.objects.filter(category='Trending')))

def diversed(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Diversed')))
