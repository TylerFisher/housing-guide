# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Dorm.percent_freshmen'
        db.delete_column(u'guide_dorm', 'percent_freshmen')

        # Deleting field 'Dorm.percent_juniors'
        db.delete_column(u'guide_dorm', 'percent_juniors')

        # Deleting field 'Dorm.percent_seniors'
        db.delete_column(u'guide_dorm', 'percent_seniors')

        # Deleting field 'Dorm.percent_sophomores'
        db.delete_column(u'guide_dorm', 'percent_sophomores')

        # Adding field 'Dorm.num_freshmen'
        db.add_column(u'guide_dorm', 'num_freshmen',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.num_sophomores'
        db.add_column(u'guide_dorm', 'num_sophomores',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.num_juniors'
        db.add_column(u'guide_dorm', 'num_juniors',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.num_seniors'
        db.add_column(u'guide_dorm', 'num_seniors',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Dorm.percent_freshmen'
        db.add_column(u'guide_dorm', 'percent_freshmen',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Dorm.percent_juniors'
        db.add_column(u'guide_dorm', 'percent_juniors',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Dorm.percent_seniors'
        db.add_column(u'guide_dorm', 'percent_seniors',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Dorm.percent_sophomores'
        db.add_column(u'guide_dorm', 'percent_sophomores',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Deleting field 'Dorm.num_freshmen'
        db.delete_column(u'guide_dorm', 'num_freshmen')

        # Deleting field 'Dorm.num_sophomores'
        db.delete_column(u'guide_dorm', 'num_sophomores')

        # Deleting field 'Dorm.num_juniors'
        db.delete_column(u'guide_dorm', 'num_juniors')

        # Deleting field 'Dorm.num_seniors'
        db.delete_column(u'guide_dorm', 'num_seniors')


    models = {
        u'guide.dorm': {
            'Meta': {'object_name': 'Dorm'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'campus_side': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'dining': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dist_to_bk': ('django.db.models.fields.FloatField', [], {}),
            'dist_to_kresge': ('django.db.models.fields.FloatField', [], {}),
            'dist_to_norris': ('django.db.models.fields.FloatField', [], {}),
            'dist_to_tech': ('django.db.models.fields.FloatField', [], {}),
            'dorm_type': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'doubles': ('django.db.models.fields.IntegerField', [], {}),
            'female_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'freshmen_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_ac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'num_freshmen': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'num_juniors': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'num_seniors': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'num_sophomores': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'open_gender': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'singles': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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
            'source': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'guide.room': {
            'Meta': {'object_name': 'Room'},
            'dorm': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['guide.Dorm']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guide.slideshowimage': {
            'Meta': {'object_name': 'SlideshowImage'},
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guide.Dorm']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['guide']