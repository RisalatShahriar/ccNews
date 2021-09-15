from userID.delete import delete_data
from django.shortcuts import render, redirect
from registration import models
from django.contrib.auth import logout
from publish import models as news_models
from django.contrib.auth.models import User
from . import delete


def userID_home(req, ID):
    if req.method == "POST":
        if req.POST['_method'] == 'delete':
            delete_news = news_models.News.objects.get(id=req.POST['_content'])
            delete.delete_data(str(f'media/{delete_news.picture}'))
            delete_news.delete()
        elif req.POST['_method'] == 'user':
            delete_user = models.Data.objects.get(accessID=req.POST['_content'])
            delete_auth = User.objects.get(username=req.POST['_content'])
            delete.delete_data(str(f'media/{delete_user.image}'))
            delete_user.delete()
            delete_auth.delete()
        elif req.POST["_method"] == 'approve':
            approve = news_models.News.objects.get(id=req.POST['_news'])
            approve.state = True
            approve.save()
        else:
            logout(req)
        return redirect('login')
    elif req.user.is_authenticated and str(req.user) == ID:
        user_info = models.Data.objects.get(accessID=ID)
        all_user = models.Data.objects.all()
        notifications = news_models.News.objects.all()
        post = user_info.post
        pic = user_info.image
        url = f'/user/{ID}'
        return render(req, 'user.html', {
            "ID": ID,
            "POST": post,
            "PROFILE": pic,
            "acc_url": url,
            "contents": notifications,
            "users": all_user
        })
    else:
        return redirect('denied')