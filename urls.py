from homesite.models import About, Services, Settings
from django.conf.urls.defaults import patterns, url, include
from django.views.generic.list import ListView
from homesite.feed import BlogRss
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Settings.objects.all()[0],
                                context_object_name="home",
                                template_name="home.html")),

    url(r'^about/', ListView.as_view(queryset=About.objects.all()[0],
                                     context_object_name="about",
                                     template_name="about.html")),

    url(r'^skills/', ListView.as_view(queryset=Services.objects.all(),
                                        context_object_name="skills",
                                        template_name="skills.html")),
    
    url(r'^contacts/',  ListView.as_view(queryset=Settings.objects.all()[0],
                                         context_object_name="contacts",
                                         template_name="contacts.html")),
    url(r'^blog/rss/$', BlogRss()),
    url(r'^blog/post/(\d+)', 'homesite.views.blog_post'),
    url(r'^blog/', 'homesite.views.blog_list'),
    url(r'^ajax/quick-form', 'homesite.views.quick_form'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)