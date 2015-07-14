from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    affiliation = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='user_images', blank=True)

    def __unicode__(self):
        return self.user.username


