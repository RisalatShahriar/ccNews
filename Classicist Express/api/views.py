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

def home_data_top(req):
    return HttpResponse(helper.api_send(models.News.objects.all().order_by('click').reverse()[:3]))

def bdaffair_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Bangladesh Affairs').order_by('click').reverse[:3]))

def cultural_insights_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Cultural Insights').order_by('click').reverse()[:3]))

def sports_insights_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Sports Insight').order_by('click').reverse()[:3]))

def internatioal_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='International Affairs').order_by('click').reverse()[:3]))

def interviews_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Small Talk With Gems').order_by('click').reverse()[:3]))

def cc_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Cultural Classicists').order_by('click').reverse()[:3]))

def youth_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Youth').order_by('click').reverse()[:3]))

def district_insights_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='District Insights').order_by('click').reverse()[:3]))

def comics_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Comics').order_by('click').reverse()[:3]))

def trending_top(req):
    return HttpResponse(helper(models.News.objects.filter(category='Trending').order_by('click').reverse()[:3]))

def diversed_top(req):
    return HttpResponse(helper.api_send(models.News.objects.filter(category='Diversed').order_by('click').reverse()[:3]))
