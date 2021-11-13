from django.shortcuts import render

from .models import Sponsor, TechSession


def index(request):
    diamond = Sponsor.objects.filter(level='Diamond')
    sapphire = Sponsor.objects.filter(level='Sapphire')
    gold = Sponsor.objects.filter(level='Gold')
    keynote_session = TechSession.objects.filter(session_type='Keynote')
    sponsor_session = TechSession.objects.filter(session_type='Sponsor')
    context = {'index_current': 'current', 'diamond': diamond, 'sapphire': sapphire,
               'gold': gold,
               'keynote': keynote_session, 'sponsor': sponsor_session}
    return render(request, 'index.html', context)


def about(request):
    context = {'about_current': 'current'}
    return render(request, 'about.html', context)


def sponsors(request):
    diamond = Sponsor.objects.filter(level='Diamond')
    sapphire = Sponsor.objects.filter(level='Sapphire')
    gold = Sponsor.objects.filter(level='Gold')
    context = {'sponsor_current': 'current', 'diamond': diamond, 'sapphire': sapphire,
               'gold': gold}
    return render(request, 'sponsors.html', context)


def session_detail(request, session_id):
    session = TechSession.objects.get(id=session_id)
    context = {'session': session}
    return render(request, 'session_detail.html', context)


def session_schedule(request):
    keynote = TechSession.objects.filter(session_type='Keynote')
    tech_session = TechSession.objects.filter(session_type='Tech')
    day1 = tech_session.filter(open_date='2021-12-07')
    day2 = tech_session.filter(open_date='2021-12-08')
    day3 = tech_session.filter(open_date='2021-12-09')
    context = {'keynote': keynote, 'day1': day1, 'day2': day2, 'day3': day3}
    return render(request, 'sessions.html', context)


def bof_schedule(request):
    return render(request, 'bof_schedule.html')


def sponsornight_schedule(request):
    return render(request, 'sponsornight_schedule.html')


def sponsor_night_introduce(request):
    diamond = Sponsor.objects.filter(level='Diamond')
    return render(request, 'sponsor_night_introduce.html', {'diamond': diamond})


def bof_introduce(request):
    diamond = Sponsor.objects.filter(level='Diamond')
    return render(request, 'bof_introduce.html', {'diamond': diamond})
