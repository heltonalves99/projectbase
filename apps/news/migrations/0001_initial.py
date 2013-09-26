# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
            ('image_home', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'news', ['News'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'news_news')


    models = {
        u'news.news': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'News'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_home': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['news']