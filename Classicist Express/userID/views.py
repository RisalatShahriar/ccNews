from django.shortcuts import render, redirect
from django.http import HttpResponse


def userID_home(req, ID):
    if req.user.is_authenticated and str(req.user) == ID:
        print(req.user)
        return render(req, 'user.html', {
            "ID": ID
        })
    else:
        return redirect('denied')
