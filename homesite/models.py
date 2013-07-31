# -*- coding: utf-8 -*-
from django.db import models


class Settings(models.Model):
    facebook = models.CharField(max_length=100,
                                verbose_name=u"Facebook profile")
    twitter = models.CharField(max_length=100,
                               verbose_name=u"Twitter profile")
    github = models.CharField(max_length=100,
                              verbose_name=u"Github profile")
    jabber = models.CharField(max_length=100,
                              verbose_name=u"Jabber")
    icq = models.CharField(max_length=100,
                           verbose_name=u"ICQ")
    email = models.CharField(max_length=100,
                             verbose_name=u"E-mail")
    skype = models.CharField(max_length=100,
                             verbose_name=u"Skype")
    cv = models.FileField(upload_to=".", verbose_name=u"CV", blank=True)
    linkedin = models.CharField(max_length=100, verbose_name=u"LinkedIn")

    class Meta:
        verbose_name = u"Settings"
        verbose_name_plural = u"Settings"

    def __unicode__(self):
        return u"Settings"


class About(models.Model):
    description = models.TextField(max_length=1000,
                                   verbose_name=u"Description")

    class Meta:
        verbose_name = u"About"
        verbose_name_plural = u"About"

    def __unicode__(self):
        return u"About"


class QuickMessages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,
                              error_messages={
                                  "null": "Enter email pls",
                                  "invalid_choice": "Enter correct email"
                              })
    message = models.TextField(max_length=1000, default=u"Message")

    class Meta:
        verbose_name = u"Messages"
        verbose_name_plural = u"Messages"

    def __unicode__(self):
        return self.message[:40]


class Blog(models.Model):
    title = models.CharField(max_length=1000, verbose_name=u"Title")
    text = models.TextField(verbose_name=u"Text")

    class Meta:
        verbose_name = u"Post"
        verbose_name_plural = u"Blog"
        ordering = ["-id"]

    def get_absolute_url(self):
        return "/blog/post/%i/" % self.id

    def __unicode__(self):
        return self.title
