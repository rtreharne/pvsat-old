from django.db import models
from sorl.thumbnail import ImageField
from time import time

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    pic = ImageField(upload_to='blog_images', blank=True)

    def __unicode__(self):
        return self.title

