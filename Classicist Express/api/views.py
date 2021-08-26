from django.http import HttpResponse
from publish import models
from . import helper
import json


# Create your views here.
def home_data(req):
    pass

def bdaffair(req):
    news = models.News.objects.filter(category='Bangladesh Affairs')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))

def cultural_insights(req):
    news = models.News.objects.filter(category='Cultural Insights')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))

def sports_insights(req):
    news = models.News.objects.filter(category='Sports Insight')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))

def achievements(req):
    news = models.News.objects.filter(category='International Affairs')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))

def interviews(req):
    news = models.News.objects.filter(category='Small Talk With Gems')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))

def cc(req):
    news = models.News.objects.filter(category='Cultural Classicists')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))

def youth(req):
    news = models.News.objects.filter(category='Youth')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))


def district_insights(req):
    news = models.News.objects.filter(category='District Insights')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))


def comics(req):
    news = models.News.objects.filter(category='Comics')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))

def trending(req):
    news = models.News.objects.filter(category='Trending')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))


def diversed(req):
    news = models.News.objects.filter(category='Diversed')
    send_api = {
        'heading': {},
        'news': {},
        'tags': {},
        'picture': {}
    }
    count = 1
    for i in news:
        helper.appender(send_api, i, count)
        count += 1
    return HttpResponse(json.dumps(send_api))
