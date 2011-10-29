# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Portfolio'
        db.delete_table('homesite_portfolio')


    def backwards(self, orm):
        
        # Adding model 'Portfolio'
        db.create_table('homesite_portfolio', (
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['homesite.Services'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('homesite', ['Portfolio'])


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
