from django.shortcuts import render
from publish import models

# Create your views here.
def readMore_page(req, link):
    news = models.News.objects.get(id=link)
    news.click += 1
    news.save()
    return render(req, 'readmore.html', {
        'HEADING': news.heading,
        'NEWS': news.news,
        'PIC': news.picture,
        "NAME": news.name
    })
