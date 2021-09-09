from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def login_page(req):
    if req.user.is_authenticated is not True:
        if req.method == 'POST':
            user = authenticate(username=req.POST['id'], password=req.POST['password'])
            if user is not None:
                login(req, user)
                if req.user.is_authenticated:
                    return redirect(f"/user/{req.POST['id']}")

            else:
                return render(req, 'login.html', {
                    "warning": True
                })
        else:
            return render(req, 'login.html')
    else:
        return redirect(f"/user/{req.POST['id']}")
