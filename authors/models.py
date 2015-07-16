from django.db import models
from django.contrib.auth.models import User
5
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    affiliation = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='user_images', default='static/img/avatar.png')
    url = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    

    def __unicode__(self):
        return self.user.username

class Abstract(models.Model):
    #unique_id = ??    
    author = models.ForeignKey(User)
    title = models.CharField(max_length=1000)
    abstract = models.TextField(max_length=5000)
    upload = models.FileField(upload_to='abstract_uploads', blank=True)
    
    DELIVERY_CHOICE = (('Oral', 'Oral'), ('Poster', 'Poster'))
    delivery = models.CharField(max_length=6, choices=DELIVERY_CHOICE, default='Oral')

    STATUS = (('Awaiting Decision', 'Awaiting decision'), ('Accepted', 'Accept'), ('Rejected', 'Reject') )
    status = models.CharField(max_length=25, choices=STATUS, default='Awaiting Decision')


    def __unicode__(self):
        return self.title
    


