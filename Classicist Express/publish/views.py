from django.shortcuts import render

# Create your views here.
def publish_page(req):
    return render(req, 'publish.html')
