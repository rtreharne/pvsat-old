from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()

    def __unicode__(self):
        return self.name
