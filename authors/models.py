from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    affiliation = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='user_images', blank=True)

    def __unicode__(self):
        return self.user.username

class Abstract(models.Model):
    #unique_id = ??    
    author = models.ForeignKey(User)
    title = models.CharField(max_length=1000)
    abstract = models.TextField(max_length=5000)
    upload = models.FileField(upload_to='abstract_uploads', blank=True)

    ORAL = 'OR'
    POSTER = 'PO'
    DELIVERY_CHOICE = ((ORAL, 'Oral'), (POSTER, 'Poster'))
    delivery = models.CharField(max_length=2, choices=DELIVERY_CHOICE, default=ORAL)
    STATUS = (('ACCEPT', 'Accept'), ('REJECT', 'Reject'), ('AWAIT', 'Awaiting decision'))
    YES_OR_NO = (('YES', 'Yes'), ('NO', 'No'))
    status = models.CharField(max_length=3, choices=STATUS, default='AWAIT')

    def __unicode__(self):
        return self.title
    


