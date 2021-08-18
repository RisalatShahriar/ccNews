from django.shortcuts import render

# Create your views here.
def userID_home(req, ID):
    return render(req, 'user.html', {
        'ID': ID
    })
