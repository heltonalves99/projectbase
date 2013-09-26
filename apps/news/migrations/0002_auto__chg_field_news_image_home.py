# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'News.image_home'
        db.alter_column(u'news_news', 'image_home', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'News.image_home'
        db.alter_column(u'news_news', 'image_home', self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100))

    models = {
        u'news.news': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'News'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_home': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['news']