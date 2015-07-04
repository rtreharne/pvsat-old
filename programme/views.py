from django.shortcuts import render
from programme.models import Speaker, Theme
from exhibitors.models import Exhibitor
from sponsors.models import Sponsor

def programme(request):
    speakers = Speaker.objects.all()
    themes = Theme.objects.all()
    exhibitors = Exhibitor.objects.all()
    sponsors = Sponsor.objects.all()
    programme_dict = {'speakers': speakers,
                      'themes': themes,
                      'exhibitors': exhibitors,
                      'sponsors': sponsors}
    return render(request, 'programme.html', programme_dict)


