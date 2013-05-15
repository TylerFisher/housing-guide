# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Dorm.video_embed'
        db.add_column(u'guide_dorm', 'video_embed',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Deleting field 'SlideshowImage.image'
        db.delete_column(u'guide_slideshowimage', 'image')

        # Deleting field 'SlideshowImage.caption'
        db.delete_column(u'guide_slideshowimage', 'caption')

        # Adding field 'SlideshowImage.url'
        db.add_column(u'guide_slideshowimage', 'url',
                      self.gf('django.db.models.fields.URLField')(default=1, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Dorm.video_embed'
        db.delete_column(u'guide_dorm', 'video_embed')

        # Adding field 'SlideshowImage.image'
        db.add_column(u'guide_slideshowimage', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'SlideshowImage.caption'
        db.add_column(u'guide_slideshowimage', 'caption',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SlideshowImage.url'
        db.delete_column(u'guide_slideshowimage', 'url')


    models = {
        u'guide.dorm': {
            'Meta': {'object_name': 'Dorm'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'campus_side': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dining': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dist_to_bk': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dist_to_kresge': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dist_to_norris': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dist_to_tech': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dorm_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'doubles': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'female_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'freshmen': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'freshmen_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_ac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'juniors': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'open_gender': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'room_dimensions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'seniors': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'singles': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '51', 'blank': 'True'}),
            'sophomores': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'triples': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'video_embed': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'guide.dormshapes': {
            'Meta': {'object_name': 'DormShapes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'osm_id': ('django.db.models.fields.FloatField', [], {}),
            'poly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {})
        },
        u'guide.quote': {
            'Meta': {'object_name': 'Quote'},
            'dorm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guide.Dorm']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guide.slideshowimage': {
            'Meta': {'object_name': 'SlideshowImage'},
            'dorm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guide.Dorm']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['guide']