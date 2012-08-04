# -*- coding: utf-8 -*-
from feed import BlogRss
from models import About, Services, Settings
from django.conf.urls import patterns, url
from django.views.generic.list import ListView


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Settings,
        context_object_name="home",
        template_name="home.haml")),
    url(r'^about/', ListView.as_view(queryset=About.objects.all(),
        context_object_name="about",
        template_name="about.haml")),
    url(r'^skills/', ListView.as_view(queryset=Services.objects.all(),
        context_object_name="skills",
        template_name="skills.haml")),
    url(r'^contacts/', ListView.as_view(model=Settings,
        template_name="contacts.haml")),
    url(r'^blog/rss/$', BlogRss()),
    url(r'^blog/post/(\d+)', 'homesite.views.blog_post'),
    url(r'^blog/', 'homesite.views.blog_list'),
    url(r'^ajax/quick-form', 'homesite.views.quick_form'),
)
