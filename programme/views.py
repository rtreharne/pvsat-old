from django.shortcuts import render
from programme.models import Speaker, Theme
from exhibitors.models import Exhibitor
from sponsors.models import Sponsor
from authors.models import UserProfile, Abstract
from django.contrib.auth.models import User

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

def abstract(request, abstract_id=1):
     abstract = Abstract.objects.get(id=abstract_id)
     profile = UserProfile.objects.get(user_id = abstract.author.id)
     dictionary = {'abstract': abstract,
                   'profile': profile}
     return render(request, 'abstract.html', dictionary)


