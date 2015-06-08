from django.shortcuts import render
from sponsors.models import Sponsor

def home(request):
    sponsor_list = Sponsor.objects.all()
    sponsor_dict = {'sponsors': sponsor_list}
    return render(request, 'home.html', sponsor_dict)
