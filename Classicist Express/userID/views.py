from django.shortcuts import render, redirect
from django.http import HttpResponse
from registration import models
from django.contrib.auth import logout
from publish import models as news_models


def userID_home(req, ID):
    if req.method == "POST":
        if req.POST['_method'] == 'delete':
            delete_news = news_models.News.objects.get(id=req.POST['_content'])
            delete_news.delete()
        else:
            logout(req)
        return redirect('login')
    elif req.user.is_authenticated and str(req.user) == ID:
        user_info = models.Data.objects.get(accessID=ID)
        notifications = news_models.News.objects.all()
        post = user_info.post
        pic = user_info.image
        url = f'/user/{ID}'
        return render(req, 'user.html', {
            "ID": ID,
            "POST": post,
            "PROFILE": pic,
            "acc_url": url,
            "contents": notifications
        })
    else:
        return redirect('denied')