from django.shortcuts import render
from datetime import datetime as date
import pytz

today = date.now(tz=pytz.timezone('Asia/Dhaka')).strftime("%B %d, %Y")


# Create your views here.
def home(req):
    return render(req, 'home.html', {
        'TITLE': 'The Classicist Express',
        'api': 'home',
        'date': today
    })

def bdaffair_page(req):
    return render(req, 'bd.html', {
        'TITLE': 'Bangladesh | The Classicist Express',
        'api': 'bd',
        'date': today
    })

def cultural_insights_page(req):
    return render(req, 'cultural.html', {
        'TITLE': 'Cultural | The Classicist Express',
        'api': 'cultural',
        'date': today
    })

def sports_insights_page(req):
    return render(req, 'sports.html', {
        'TITLE': 'Sports | The Classicist Express',
        'api': 'sports',
        'date': today
    })

def internatioal_page(req):
    return render(req, 'international.html', {
        'TITLE': 'International | The Classicist Express',
        'api': 'international',
        'date': today
    })

def interviews_page(req):
    return render(req, 'interview.html', {
        'TITLE': 'Interview | The Classicist Express',
        'api': 'interview',
        'date': today
    })

def cc_page(req):
    return render(req, 'cc.html', {
        'TITLE': 'Cultural Classicist | The Classicist Express',
        'api': 'cc',
        'date': today
    })

def youth_page(req):
    return render(req, 'youth.html', {
        'TITLE': 'Youth | The Classicist Express',
        'api': 'youth',
        'date': today
    })

def district_insights_page(req):
    return render(req, 'district.html', {
        'TITLE': 'Dictrict | The Classicist Express',
        'api': 'district',
        'date': today
    })

def comics_page(req):
    return render(req, 'comics.html', {
        'TITLE': 'Comics | The Classicist Express',
        'api': 'comics',
        'date': today
    })

def trending_page(req):
    return render(req, 'trending.html', {
        'TITLE': 'Trending | The Classicist Express',
        'api': 'trending',
        'date': today
    })

def diversed_page(req):
    return render(req, 'diversed.html', {
        'TITLE': 'Diversed | The Classicist Express',
        'api': 'diversed',
        'date': today
    })
