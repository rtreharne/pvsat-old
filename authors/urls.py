from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^register/$', 'authors.views.register', name='register'),
    url(r'^login/$', 'authors.views.user_login', name='login'),
)
