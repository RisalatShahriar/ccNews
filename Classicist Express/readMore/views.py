from django.shortcuts import render
from django.utils.regex_helper import flatten_result
from publish import models
from datetime import date

today = date.today().strftime("%B %d, %Y")

# Create your views here.
def readMore_page(req, link):
    news = models.News.objects.get(id=link)
    if news.state == 1:
        news.click += 1
        news.save()
        return render(req, 'readmore.html', {
            'HEADING': news.heading,
            'NEWS': news.news,
            'PIC': news.picture,
            "NAME": news.name,
            'time': today
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
