# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dorm'
        db.create_table(u'guide_dorm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dorm_type', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('has_ac', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('campus_side', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('dining', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('female_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('freshmen_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('open_gender', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('percent_freshmen', self.gf('django.db.models.fields.FloatField')()),
            ('percent_sophomores', self.gf('django.db.models.fields.FloatField')()),
            ('percent_juniors', self.gf('django.db.models.fields.FloatField')()),
            ('percent_seniors', self.gf('django.db.models.fields.FloatField')()),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('blurb', self.gf('django.db.models.fields.TextField')()),
            ('singles', self.gf('django.db.models.fields.IntegerField')()),
            ('doubles', self.gf('django.db.models.fields.IntegerField')()),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('master', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('dist_to_tech', self.gf('django.db.models.fields.FloatField')()),
            ('dist_to_norris', self.gf('django.db.models.fields.FloatField')()),
            ('dist_to_bk', self.gf('django.db.models.fields.FloatField')()),
            ('dist_to_kresge', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'guide', ['Dorm'])

        # Adding model 'Quote'
        db.create_table(u'guide_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('source', self.gf('django.db.models.fields.TextField')()),
            ('dorm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guide.Dorm'], null=True, blank=True)),
        ))
        db.send_create_signal(u'guide', ['Quote'])

        # Adding model 'Room'
        db.create_table(u'guide_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'guide', ['Room'])

        # Adding M2M table for field dorm on 'Room'
        db.create_table(u'guide_room_dorm', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('room', models.ForeignKey(orm[u'guide.room'], null=False)),
            ('dorm', models.ForeignKey(orm[u'guide.dorm'], null=False))
        ))
        db.create_unique(u'guide_room_dorm', ['room_id', 'dorm_id'])

        # Adding model 'SlideshowImage'
        db.create_table(u'guide_slideshowimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guide.Dorm'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'guide', ['SlideshowImage'])

        # Adding model 'DormShapes'
        db.create_table(u'guide_dormshapes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('osm_id', self.gf('django.db.models.fields.FloatField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('poly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'guide', ['DormShapes'])


    def backwards(self, orm):
        # Deleting model 'Dorm'
        db.delete_table(u'guide_dorm')

        # Deleting model 'Quote'
        db.delete_table(u'guide_quote')

        # Deleting model 'Room'
        db.delete_table(u'guide_room')

        # Removing M2M table for field dorm on 'Room'
        db.delete_table('guide_room_dorm')

        # Deleting model 'SlideshowImage'
        db.delete_table(u'guide_slideshowimage')

        # Deleting model 'DormShapes'
        db.delete_table(u'guide_dormshapes')


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
            'open_gender': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'percent_freshmen': ('django.db.models.fields.FloatField', [], {}),
            'percent_juniors': ('django.db.models.fields.FloatField', [], {}),
            'percent_seniors': ('django.db.models.fields.FloatField', [], {}),
            'percent_sophomores': ('django.db.models.fields.FloatField', [], {}),
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