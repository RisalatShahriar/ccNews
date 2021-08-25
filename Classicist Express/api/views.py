from django.http import HttpResponse
from publish import models
from . import helper
import json


# Create your views here.
def home_data(req):
    pass

def bdaffair(req):
    news = models.News.objects.filter(category='Bangladesh Affairs')
    send_list_api = []
    for i in news:
        helper.appender(send_list_api, i)
    return HttpResponse(json.dumps(send_list_api))
