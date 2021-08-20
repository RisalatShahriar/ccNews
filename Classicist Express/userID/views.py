from django.shortcuts import render
from django.http import HttpResponse


def userID_home(req, ID):
    if req.user.is_authenticated and str(req.user) == ID:
        print(req.user)
        return render(req, 'user.html', {
            "ID": ID
        })
    else:
        return HttpResponse("Access Denied")
