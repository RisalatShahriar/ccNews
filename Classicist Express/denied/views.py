from django.shortcuts import render, redirect


# Create your views here.
def denied(req):
    if not req.user.is_authenticated:
        return render(req, 'denied.html')
    else:
        return redirect('home')
