from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req, 'home.html', {
        'TITLE': 'Home | Classicist Express'
    })

def bdaffair_page(req):
    return render(req, 'bd.html', {
        'TITLE': 'Bangladesh | Classicist Express'
    })

def cultural_insights_page(req):
    return render(req, 'cultural.html', {
        'TITLE': 'Cultural | Classicist Express'
    })

def sports_insights_page(req):
    return render(req, 'sports.html', {
        'TITLE': 'Sports | Classicist Express'
    })

def internatioal_page(req):
    return render(req, 'international.html', {
        'TITLE': 'International | Classicist Express'
    })

def interviews_page(req):
    return render(req, 'interview.html', {
        'TITLE': 'Interview | Classicist Express'
    })

def cc_page(req):
    return render(req, 'cc.html', {
        'TITLE': 'Cultural Classicist | Classicist Express'
    })

def youth_page(req):
    return render(req, 'youth.html', {
        'TITLE': 'Youth | Classicist Express'
    })

def district_insights_page(req):
    return render(req, 'district.html', {
        'TITLE': 'Dictrict | Classicist Express'
    })

def comics_page(req):
    return render(req, 'comics.html', {
        'TITLE': 'Comics | Classicist Express'
    })

def trending_page(req):
    return render(req, 'trending.html', {
        'TITLE': 'Trending | Classicist Express'
    })

def diversed_page(req):
    return render(req, 'diversed.html', {
        'TITLE': 'Diversed | Classicist Express'
    })
