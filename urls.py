from django.conf.urls import patterns, url, include
from django.contrib import admin
import settings

admin.autodiscover()

handler404 = 'homesite.views.error404'
handler500 = 'homesite.views.error500'

urlpatterns = patterns('',
    url(r'', include('homesite.urls')),
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
    ),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}
    ),
    url(r'^admin/', include(admin.site.urls)),
)
