from django.conf.urls import patterns, url, include
from django.contrib import admin
import settings

admin.autodiscover()

handler404 = 'homesite.views.error404'
handler500 = 'homesite.views.error500'

urlpatterns = patterns('',
    url(r'', include('homesite.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
