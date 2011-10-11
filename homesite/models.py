# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image
import settings

class Services(models.Model):
    '''
    fields: title, description, image
    '''
    title = models.CharField(max_length=1000, verbose_name=u'Name (for select in Portfolio)')
    description = models.TextField(max_length=1000, verbose_name=u'Description')
    image = models.ImageField(upload_to='services', verbose_name=u'Image', blank=True)

    def save(self, size=(100, 100)):
        super(Services, self).save()
        filename = '%s/%s' % (settings.MEDIA_ROOT, self.image)
        image = Image.open(filename)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename)

    class Meta:
        verbose_name = u'Service'
        verbose_name_plural = u'Services'

    def __unicode__(self):
        return self.title

class Portfolio(models.Model):
    '''
    fields: title, description, type, link, image
    '''
    title = models.CharField(max_length=1000, verbose_name=u'Name')
    description = models.TextField(max_length=1000, verbose_name=u'Description')
    type = models.ForeignKey(Services, blank=True, verbose_name=u'Type')
    link = models.URLField(verbose_name=u'Link')
    image = models.ImageField(upload_to='portfolio', verbose_name=u'Image', blank=True)

    class Meta:
        verbose_name = u'Portfolio'
        verbose_name_plural = u'Portfolio'

    def save(self, size=(250, 250)):
        super(Portfolio, self).save()
        filename = '%s/%s' % (settings.MEDIA_ROOT, self.image)
        image = Image.open(filename)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename)

    def __unicode__(self):
        return self.title

class Settings(models.Model):
    '''
    fields: home_portfolio, home_services, home_about, home_contacts, facebook, twitter, github, jabber,
    icq, email, skype, cv
    '''
    home_portfolio = models.TextField(max_length=1000, verbose_name=u'Portfolio (small)')
    home_services = models.TextField(max_length=1000, verbose_name=u'Services (small)')
    home_about = models.TextField(max_length=1000, verbose_name=u'About (small)')
    home_contacts = models.TextField(max_length=1000, verbose_name=u'Contacts (small)')
    facebook = models.CharField(max_length=100, verbose_name=u'Facebook profile')
    twitter = models.CharField(max_length=100, verbose_name=u'Twitter profile')
    github = models.CharField(max_length=100, verbose_name=u'Github profile')
    jabber = models.CharField(max_length=100, verbose_name=u'Jabber')
    icq = models.CharField(max_length=100, verbose_name=u'ICQ')
    email = models.CharField(max_length=100, verbose_name=u'E-mail')
    skype = models.CharField(max_length=100, verbose_name=u'Skype')
    cv = models.FileField(upload_to='.', verbose_name=u'CV', blank=True)

    class Meta:
        verbose_name = u'Settings'
        verbose_name_plural = u'Settings'

    def __unicode__(self):
        return u'Settings'

class About(models.Model):
    '''
    fields: description
    '''
    description = models.TextField(max_length=1000, verbose_name=u'Description')

    class Meta:
        verbose_name = u'About'
        verbose_name_plural = u'About'

    def __unicode__(self):
        return u'About'

class QuickMessages(models.Model):
    '''
    fields: name, email, message
    '''
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, error_messages={'null':'Enter email pls','invalid_choice':'Enter correct email'})
    message = models.TextField(max_length=1000, default=u'Message')

    class Meta:
        verbose_name = u'Messages'
        verbose_name_plural = u'Messages'

    def __unicode__(self):
        return self.message[:40]

class Blog(models.Model):
    '''
    fields: title, text 
    '''
    title = models.CharField(max_length=1000,verbose_name=u'Title')
    text = models.TextField(verbose_name=u'Text', )

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Blog'

    def get_absolute_url(self):
        return "/blog/post/%i/" % self.id

    def __unicode__(self):
        return self.title