# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Content'
        db.create_table(u'content_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('father', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'pai', null=True, to=orm['content.Content'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'content', ['Content'])


    def backwards(self, orm):
        # Deleting model 'Content'
        db.delete_table(u'content_content')


    models = {
        u'content.content': {
            'Meta': {'object_name': 'Content'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'pai'", 'null': 'True', 'to': u"orm['content.Content']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['content']