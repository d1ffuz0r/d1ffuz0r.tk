# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Services'
        db.create_table('homesite_services', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('homesite', ['Services'])

        # Adding model 'Portfolio'
        db.create_table('homesite_portfolio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['homesite.Services'], blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('homesite', ['Portfolio'])

        # Adding model 'Settings'
        db.create_table('homesite_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('icq', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('homesite', ['Settings'])

        # Adding model 'About'
        db.create_table('homesite_about', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal('homesite', ['About'])

        # Adding model 'QuickMessages'
        db.create_table('homesite_quickmessages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('message', self.gf('django.db.models.fields.TextField')(default=u'Message', max_length=1000)),
        ))
        db.send_create_signal('homesite', ['QuickMessages'])

        # Adding model 'Blog'
        db.create_table('homesite_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('homesite', ['Blog'])


    def backwards(self, orm):
        
        # Deleting model 'Services'
        db.delete_table('homesite_services')

        # Deleting model 'Portfolio'
        db.delete_table('homesite_portfolio')

        # Deleting model 'Settings'
        db.delete_table('homesite_settings')

        # Deleting model 'About'
        db.delete_table('homesite_about')

        # Deleting model 'QuickMessages'
        db.delete_table('homesite_quickmessages')

        # Deleting model 'Blog'
        db.delete_table('homesite_blog')


    models = {
        'homesite.about': {
            'Meta': {'object_name': 'About'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'homesite.blog': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Blog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'homesite.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['homesite.Services']", 'blank': 'True'})
        },
        'homesite.quickmessages': {
            'Meta': {'object_name': 'QuickMessages'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'default': "u'Message'", 'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'homesite.services': {
            'Meta': {'object_name': 'Services'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'homesite.settings': {
            'Meta': {'object_name': 'Settings'},
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['homesite']
