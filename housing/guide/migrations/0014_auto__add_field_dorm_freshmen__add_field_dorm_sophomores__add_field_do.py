# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Dorm.freshmen'
        db.add_column(u'guide_dorm', 'freshmen',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.sophomores'
        db.add_column(u'guide_dorm', 'sophomores',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.juniors'
        db.add_column(u'guide_dorm', 'juniors',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.seniors'
        db.add_column(u'guide_dorm', 'seniors',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Dorm.freshmen'
        db.delete_column(u'guide_dorm', 'freshmen')

        # Deleting field 'Dorm.sophomores'
        db.delete_column(u'guide_dorm', 'sophomores')

        # Deleting field 'Dorm.juniors'
        db.delete_column(u'guide_dorm', 'juniors')

        # Deleting field 'Dorm.seniors'
        db.delete_column(u'guide_dorm', 'seniors')


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
            'triples': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dorm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guide.Dorm']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['guide']