from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'programme.views.programme', name='programme'),
    url(r'^abstracts/(?P<abstract_id>\d+)/$', 'programme.views.abstract'),
    url(r'^profiles/(?P<user_id>\d+)/$', 'programme.views.profile'),
)
