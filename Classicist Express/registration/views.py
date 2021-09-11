from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models


# Create your views here.
def check_admin(id):
    check = models.Data.objects.get(accessID=id)
    return check.post == 'Admin'


def registration_page(req):
    if req.user.is_authenticated and check_admin(str(req.user)):
        if req.method == "POST":
            if req.POST['password'] == req.POST['password2']:
                user_cred = User.objects.create_user(username=req.POST['name'], email=req.POST['email'], password=req.POST['password'])
                user_data = models.Data(accessID=req.POST['name'], email=req.POST['email'], number=req.POST['contact'], image=req.FILES.get('image'), post=req.POST.get('des'), address=req.POST['address'])
                user_cred.save()
                user_data.save()
                return render(req, 'registration.html', {
                    'id': req.user
                })
        else:
            return render(req, 'registration.html', {
                'id': req.user
            })
    else:
        return redirect('denied')
