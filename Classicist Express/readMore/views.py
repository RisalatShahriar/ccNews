from django.shortcuts import render
from publish import models

# Create your views here.
def readMore_page(req, link):
    news = models.News.objects.get(id=link)
    return render(req, 'readmore.html', {
        'HEADING': news.heading,
        'NEWS': news.news
    })
