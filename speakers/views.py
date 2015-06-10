from django.shortcuts import render
from sponsors.models import Sponsor

def home(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    sponsor_dict = {'sponsors': sponsor_list,
                    'speakers': speaker_list}
    return render(request, 'home.html', sponsor_dict)
