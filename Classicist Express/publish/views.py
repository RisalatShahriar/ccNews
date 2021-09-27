from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def publish_page(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            if req.POST['_check'] == 'Pass':
                news = models.News(category=req.POST.get('cat'), heading=req.POST['heading'], news=req.POST['news'], name=req.POST['name'], picture=req.FILES.get('picnews'), click=0, writer=req.user)
                news.save()
                return render(req, 'publish.html', {
                    'id': req.user
                })
            else:
                return HttpResponse("Something went wrong!")
        else:
            return render(req, 'publish.html', {
                'id': req.user
            })
    else:
        return redirect('denied')
