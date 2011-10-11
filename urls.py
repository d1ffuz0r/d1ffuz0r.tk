from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from homesite.feed import BlogRss
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'homesite.views.home'),
    url(r'^about/', 'homesite.views.about'),
    url(r'^portfolio/', 'homesite.views.portfolio'),
    url(r'^services/', 'homesite.views.services'),
    url(r'^contacts/', 'homesite.views.contacts'),
    url(r'^blog/rss/$', BlogRss()),
    url(r'^blog/post/(\d+)', 'homesite.views.blog_post'),
    url(r'^blog/', 'homesite.views.blog_list'),
    url(r'^ajax/quick-form', 'homesite.views.quick_form'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
 