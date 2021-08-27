from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req, 'home.html', {
        'TITLE': 'Classicist Express',
        'api': 'home'
    })

def bdaffair_page(req):
    return render(req, 'bd.html', {
        'TITLE': 'Bangladesh | Classicist Express',
        'api': 'bd'
    })

def cultural_insights_page(req):
    return render(req, 'cultural.html', {
        'TITLE': 'Cultural | Classicist Express',
        'api': 'cultural'
    })

def sports_insights_page(req):
    return render(req, 'sports.html', {
        'TITLE': 'Sports | Classicist Express',
        'api': 'sports'
    })

def internatioal_page(req):
    return render(req, 'international.html', {
        'TITLE': 'International | Classicist Express',
        'api': 'international'
    })

def interviews_page(req):
    return render(req, 'interview.html', {
        'TITLE': 'Interview | Classicist Express',
        'api': 'interview'
    })

def cc_page(req):
    return render(req, 'cc.html', {
        'TITLE': 'Cultural Classicist | Classicist Express',
        'api': 'cc'
    })

def youth_page(req):
    return render(req, 'youth.html', {
        'TITLE': 'Youth | Classicist Express',
        'api': 'youth'
    })

def district_insights_page(req):
    return render(req, 'district.html', {
        'TITLE': 'Dictrict | Classicist Express',
        'api': 'district'
    })

def comics_page(req):
    return render(req, 'comics.html', {
        'TITLE': 'Comics | Classicist Express',
        'api': 'comics'
    })

def trending_page(req):
    return render(req, 'trending.html', {
        'TITLE': 'Trending | Classicist Express',
        'api': 'trending'
    })

def diversed_page(req):
    return render(req, 'diversed.html', {
        'TITLE': 'Diversed | Classicist Express',
        'api': 'diversed'
    })
