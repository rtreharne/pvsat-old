from django.shortcuts import render
from programme.models import Speaker, Theme

def programme(request):
    speakers = Speaker.objects.all()
    themes = Theme.objects.all()
    programme_dict = {'speakers': speakers,
                      'themes': themes}
    return render(request, 'programme.html', programme_dict)


