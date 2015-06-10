from django.db import models

class Speaker(models.Model):
    forename = models.CharField(max_length=128, unique = True)
    surname = models.CharField(max_length=128, unique = True)
    affiliation = models.CharField(max_length=128)
    url = models.URLField()
    pic = models.ImageField(upload_to='logo_images', blank=True)

    def __unicode__(self):
        return self.surname
