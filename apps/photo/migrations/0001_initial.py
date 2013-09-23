# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table(u'photo_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'photo', ['Gallery'])

        # Adding model 'Image'
        db.create_table(u'photo_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photo.Gallery'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('legend', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'photo', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table(u'photo_gallery')

        # Deleting model 'Image'
        db.delete_table(u'photo_image')


    models = {
        u'photo.gallery': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Gallery'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'photo.image': {
            'Meta': {'object_name': 'Image'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photo.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'legend': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['photo']