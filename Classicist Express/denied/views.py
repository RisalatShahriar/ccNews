from django.shortcuts import render


# Create your views here.
def denied(req):
    return render(req, 'denied.html')
