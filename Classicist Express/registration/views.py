from django.shortcuts import render

# Create your views here.
def registration_page(req):
    return render(req, 'registration.html')