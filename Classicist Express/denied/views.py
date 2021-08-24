from django.shortcuts import render, redirect


# Create your views here.
def denied(req):
    if not req.user.is_authenticated:
        return redirect('home')
    else:
        return render(req, 'denied.html')

