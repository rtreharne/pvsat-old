from django.shortcuts import render
from sponsors.models import Sponsor
from speakers.models import Speaker

def home(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    sponsor_dict = {'sponsors': sponsor_list,
			        'speakers': speaker_list}
    return render(request, 'home.html', sponsor_dict)

def bootstrap(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    sponsor_dict = {'sponsors': sponsor_list,
			        'speakers': speaker_list}
    return render(request, 'bootstrap.html', sponsor_dict)
