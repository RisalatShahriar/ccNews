from django.shortcuts import render
from django.http import HttpResponse
from . import models


def publish_page(req):
    if req.method == 'POST':
        if req.user.is_authenticated:
            news = models.News(category=req.POST.get('cat'), heading=req.POST['heading'],
                               news=req.POST['news'], tags=req.POST['tags'])
            news.save()
            return render(req, 'publish.html')
        else:
            return HttpResponse("Access denied")
    else:
        return render(req, 'publish.html')
