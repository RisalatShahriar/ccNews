from django.shortcuts import render, redirect
from . import models


def publish_page(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            news = models.News(category=req.POST.get('cat'), heading=req.POST['heading'], news=req.POST['news'], tags=req.POST['tags'])
            news.save()
            return render(req, 'publish.html')
        else:
            return render(req, 'publish.html')
    else:
        return redirect('denied')
