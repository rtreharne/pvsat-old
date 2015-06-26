from django.shortcuts import render
from sponsors.models import Sponsor
from speakers.models import Speaker
from random import shuffle

def home(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    sponsor_dict = {'sponsors': sponsor_list,
			        'speakers': speaker_list}
    return render(request, 'home.html', sponsor_dict)

def chunk(a):
    b = list(a)
    shuffle(b)
    chunk_list = []
    for i in range (0, len(b), 5):
        chunk = b[i:i+5]
        chunk_list.append(chunk)
    return chunk_list

def bootstrap(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    speaker_chunk = chunk(speaker_list)
    sponsor_dict = {'sponsors': sponsor_list,
	            'speakers': speaker_chunk}
    return render(request, 'bootstrap.html', sponsor_dict)

def bare(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    speaker_chunk = chunk(speaker_list)
    sponsor_dict = {'sponsors': sponsor_list,
	            'speakers': speaker_chunk}
    return render(request, 'bare.html', sponsor_dict)
