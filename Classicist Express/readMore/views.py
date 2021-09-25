from django.shortcuts import render
from django.utils.regex_helper import flatten_result
from publish import models
from . import models as com_mod
from datetime import datetime as date
import pytz

today = date.now(tz=pytz.timezone('Asia/Dhaka')).strftime("%B %d, %Y")

# Create your views here.
def readMore_page(req, link):
    news = models.News.objects.get(id=link)
    if news.state == 1:
        if req.method == 'POST':
            com_info = com_mod.Comment(name=req.POST['fullName'], date=today, comment=req.POST['comment'])
            com_info.save()
            return render(req, 'readmore.html', {
                'HEADING': news.heading,
                'NEWS': news.news,
                'PIC': news.picture,
                "NAME": news.name,
                'time': today,
                'acc_url': f'/readmore/{link}'
            })
        else:
            news.click += 1
            news.save()
            return render(req, 'readmore.html', {
                'HEADING': news.heading,
                'NEWS': news.news,
                'PIC': news.picture,
                "NAME": news.name,
                'time': today,
                'acc_url': f'/readmore/{link}'
            })

def readmore_approve(req, link):
    news = models.News.objects.get(id=link)
    if req.user.is_authenticated and news.state == 0:
        return render(req, 'readmore.html', {
            'HEADING': news.heading,
            'NEWS': news.news,
            'PIC': news.picture,
            "NAME": news.name,
            'time': today
        })
