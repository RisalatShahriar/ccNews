from django.shortcuts import render
from django.contrib.auth.models import User
from . import models


# Create your views here.
def registration_page(req):
    if req.method == "POST":
        if req.POST['password'] == req.POST['password2']:
            user_cred = User.objects.create_user(username=req.POST['name'], email=req.POST['email'],
                                            password=req.POST['password'])
            user_data = models.Data(accessID=req.POST['name'], email=req.POST['email'], number=req.POST['contact'],
                                    post=req.POST.get('des'), address=req.POST['address'])
            user_cred.save()
            user_data.save()
            return render(req, 'registration.html')
    else:
        return render(req, 'registration.html')
