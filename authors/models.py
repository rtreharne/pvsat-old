from django.db import models
from django.contrib.auth.models import User
from programme.models import Theme
from django.utils import timezone
from time import time
from sorl.thumbnail import get_thumbnail, ImageField

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    affiliation = models.CharField(max_length=128, blank = True)
    picture = ImageField(upload_to='user_images', default='static/img/avatar.png')
    url = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    bio = models.TextField(max_length=2000, blank=True)

    def __unicode__(self):
        return self.user.username

class Abstract(models.Model):
    author = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=1000)
    abstract = models.TextField(max_length=5000)
    upload = models.FileField(upload_to='abstract_uploads', blank=True)
    theme = models.ManyToManyField(Theme)
    
    DELIVERY_CHOICE = (('Oral', 'Oral'), ('Poster', 'Poster'))
    delivery = models.CharField(max_length=6, choices=DELIVERY_CHOICE, default='Oral')

    STATUS = (('Awaiting Decision', 'Awaiting decision'), ('Accepted', 'Accept'), ('Rejected', 'Reject') )
    status = models.CharField(max_length=25, choices=STATUS, default='Awaiting Decision')

    date = models.DateTimeField(default=timezone.datetime.today())


    def __unicode__(self):
        return self.title
    


