from django.shortcuts import render, get_object_or_404
from config.models import *


def home(req):
    profile = get_object_or_404(MyProfile, pk=1)
    social = MySocial.objects.all()
    edu = Education.objects.all().order_by('-pk')
    skill = Skill.objects.all().order_by('-pk')
    aw = Award.objects.all().order_by('-pk')
    con = {
        'profile': profile,
        'social': social,
        'edu': edu,
        'skill': skill,
        'aw': aw,
    }
    return render(req, 'main.html', con)
