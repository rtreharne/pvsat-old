from django import forms
from django.contrib.auth.models import User
from authors.models import UserProfile, Abstract

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
	fields = ('username', 'email', 'password', 'first_name', 'last_name')
        help_texts = {'username': None}
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email address has already been registered')
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('affiliation', 'picture', 'bio', 'url', 'linkedin', 'twitter')

class AbstractForm(forms.ModelForm):
    class Meta:
        model = Abstract
        fields = ('title', 'abstract', 'upload', 'delivery')
 

    

