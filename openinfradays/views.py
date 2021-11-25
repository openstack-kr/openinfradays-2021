import json

from functools import wraps
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Sponsor, TechSession, VirtualBooth


def agreement_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                if not request.user.profile.agree_with_private:
                    return redirect('/join')
            except Exception as e:
                pass
        return function(request, *args, **kwargs)
    return wrap


@agreement_required
def index(request):
    diamond = Sponsor.objects.filter(level='Diamond')
    sapphire = Sponsor.objects.filter(level='Sapphire')
    gold = Sponsor.objects.filter(level='Gold')
    keynote_session = TechSession.objects.filter(session_type='Keynote')
    sponsor_session = TechSession.objects.filter(session_type='Sponsor')
    context = {'index_current': 'current', 'diamond': diamond, 'sapphire': sapphire,
               'gold': gold,
               'keynote': keynote_session, 'sponsor': sponsor_session,
               'login': login}
    return render(request, 'index.html', context)


@agreement_required
def about(request):
    context = {'about_current': 'current'}
    return render(request, 'about.html', context)


@agreement_required
def sponsors(request):
    diamond = Sponsor.objects.filter(level='Diamond')
    sapphire = Sponsor.objects.filter(level='Sapphire')
    gold = Sponsor.objects.filter(level='Gold')
    context = {'sponsor_current': 'current', 'diamond': diamond, 'sapphire': sapphire,
               'gold': gold}
    return render(request, 'sponsors.html', context)


@csrf_exempt
def join(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('/')

        if request.user.profile.agree_with_private:
            return redirect('/')
        return render(request, 'join.html', {'user': request.user})
    elif request.method == "POST":
        body = json.loads(request.body)
        user = request.user
        user.profile.agree_with_private = True
        user.profile.agree_with_sponsor = True
        user.first_name = body['user_name']
        user.profile.company = body['user_org']
        user.profile.job = body.get('user_job', '')
        user.profile.naver_cloud_form = body.get('naver_cloud_form', '')
        if body.get('naver_cloud_agree') == 'Y':
            user.profile.is_check_navercloud = True
        user.save()
        return JsonResponse({'result': True})


@csrf_exempt
def update_profile(request):
    if request.method != "PUT" or not request.user.is_authenticated:
        return redirect('/')
    user = request.user
    body = json.loads(request.body)
    user.first_name = body['user_name']
    user.profile.company = body['user_org']
    user.profile.job = body.get('user_job', '')
    user.profile.naver_cloud_form = body.get('naver_cloud_form', '')
    if body.get('naver_cloud_agree') == 'Y':
        user.profile.is_check_navercloud = True
    user.save()
    return JsonResponse({'result': True})


@agreement_required
def virtualbooth(request):
    vb = VirtualBooth.objects.all()
    context = {'virtualbooth_current': 'current', 'virtualbooth': vb}
    return render(request, 'virtualbooth.html', context)


@agreement_required
def virtualbooth_detail(request, virtualbooth_id):
    virtualbooth = VirtualBooth.objects.get(id=virtualbooth_id)
    context = {'vb': virtualbooth}
    return render(request, 'virtualbooth_detail.html', context)


@agreement_required
def session_detail(request, session_id):
    session = TechSession.objects.get(id=session_id)
    context = {'session': session}
    return render(request, 'session_detail.html', context)


@agreement_required
def session_schedule(request):
    keynote = TechSession.objects.filter(session_type='Keynote')
    tech_session = TechSession.objects.filter(session_type='Tech')
    day1 = tech_session.filter(open_date='2021-12-07')
    day2 = tech_session.filter(open_date='2021-12-08')
    day3 = tech_session.filter(open_date='2021-12-09')
    context = {'keynote': keynote, 'day1': day1, 'day2': day2, 'day3': day3}
    return render(request, 'sessions.html', context)


@agreement_required
def bof_schedule(request):
    return render(request, 'bof_schedule.html')


@agreement_required
def sponsornight_schedule(request):
    return render(request, 'sponsornight_schedule.html')


@agreement_required
def sponsor_night_introduce(request):
    diamond = Sponsor.objects.filter(level='Diamond')
    return render(request, 'sponsor_night_introduce.html', {'diamond': diamond})


@agreement_required
def bof_introduce(request):
    diamond = Sponsor.objects.filter(level='Diamond')
    return render(request, 'bof_introduce.html', {'diamond': diamond})


@agreement_required
@csrf_exempt
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user
    return render(request, 'profile.html', {'user': user})


def login(request):
    return render(request, 'login.html', {})
