from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'stanley.views.home', name='home'),
)

if settings.DEBUG:
	urlpatterns += patterns(
			'django.views.static',
			(r'^media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT}),
                        )
