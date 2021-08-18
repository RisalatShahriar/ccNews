from django.shortcuts import render

# Create your views here.
def readMore_page(req):
    return render(req, 'readmore.html')