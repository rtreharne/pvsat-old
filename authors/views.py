from django.shortcuts import render
from authors.forms import UserForm, UserProfileForm, AbstractForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from authors.models import UserProfile, Abstract

@login_required
def submit_abstract(request):
    submitted = False

    if request.method == 'POST':
        abstract_form = AbstractForm(data=request.POST)
		
        if abstract_form.is_valid():
			abstract = abstract_form.save(commit=False)
			abstract.author= request.user

			if 'upload' in request.FILES:
			   abstract.upload = request.FILES['upload']

			abstract_form.save()

			submitted = True

        else:
			print abstract_form.errors
    
    else:	    
	    abstract_form = AbstractForm()
	
    return render(request, 'submit_abstract.html', {'abstract_form': abstract_form, 'submitted': submitted})

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Your account is disabled")

        else:
            print "Invalid login details"
            return HttpResponse("Invalid login details supplied")
                
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        else:
	    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def dashboard(request):
    user = request.user
    profile = UserProfile.objects.get(user_id=user.id)
    abstracts = Abstract.objects.filter(author=user)
    return render(request, 'dashboard.html', {'user':user, 'profile': profile, 'abstracts': abstracts})
    
