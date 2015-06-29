from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'pvsat.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns(
			'django.views.static',
			(r'^media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT}),
                        )
