# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Settings, About, QuickMessages, Blog
from django.contrib.auth.models import User, Group


class AdminServices(admin.ModelAdmin):
    pass


class AdminSettings(admin.ModelAdmin):
    pass


class AdminAbout(admin.ModelAdmin):
    pass


class AdminQuickMessage(admin.ModelAdmin):
    pass


class AdminBlog(admin.ModelAdmin):
    pass

admin.site.register(Settings, AdminSettings)
admin.site.register(About, AdminAbout)
admin.site.register(QuickMessages, AdminQuickMessage)
admin.site.register(Blog, AdminBlog)
admin.site.unregister(User)
admin.site.unregister(Group)
