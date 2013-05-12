# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Room'
        db.delete_table(u'guide_room')

        # Removing M2M table for field dorm on 'Room'
        db.delete_table('guide_room_dorm')

        # Deleting field 'Dorm.num_seniors'
        db.delete_column(u'guide_dorm', 'num_seniors')

        # Deleting field 'Dorm.num_juniors'
        db.delete_column(u'guide_dorm', 'num_juniors')

        # Deleting field 'Dorm.num_freshmen'
        db.delete_column(u'guide_dorm', 'num_freshmen')

        # Deleting field 'Dorm.num_sophomores'
        db.delete_column(u'guide_dorm', 'num_sophomores')

        # Adding field 'Dorm.room_dimensions'
        db.add_column(u'guide_dorm', 'room_dimensions',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


        # Changing field 'Dorm.dist_to_bk'
        db.alter_column(u'guide_dorm', 'dist_to_bk', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Dorm.dist_to_norris'
        db.alter_column(u'guide_dorm', 'dist_to_norris', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Dorm.style'
        db.alter_column(u'guide_dorm', 'style', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Dorm.dist_to_tech'
        db.alter_column(u'guide_dorm', 'dist_to_tech', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Dorm.dist_to_kresge'
        db.alter_column(u'guide_dorm', 'dist_to_kresge', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Dorm.campus_side'
        db.alter_column(u'guide_dorm', 'campus_side', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Dorm.dorm_type'
        db.alter_column(u'guide_dorm', 'dorm_type', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Dorm.cost'
        db.alter_column(u'guide_dorm', 'cost', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Dorm.master'
        db.alter_column(u'guide_dorm', 'master', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Dorm.singles'
        db.alter_column(u'guide_dorm', 'singles', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Dorm.address'
        db.alter_column(u'guide_dorm', 'address', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Dorm.doubles'
        db.alter_column(u'guide_dorm', 'doubles', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Dorm.blurb'
        db.alter_column(u'guide_dorm', 'blurb', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Dorm.size'
        db.alter_column(u'guide_dorm', 'size', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Adding model 'Room'
        db.create_table(u'guide_room', (
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'guide', ['Room'])

        # Adding M2M table for field dorm on 'Room'
        db.create_table(u'guide_room_dorm', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('room', models.ForeignKey(orm[u'guide.room'], null=False)),
            ('dorm', models.ForeignKey(orm[u'guide.dorm'], null=False))
        ))
        db.create_unique(u'guide_room_dorm', ['room_id', 'dorm_id'])

        # Adding field 'Dorm.num_seniors'
        db.add_column(u'guide_dorm', 'num_seniors',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.num_juniors'
        db.add_column(u'guide_dorm', 'num_juniors',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.num_freshmen'
        db.add_column(u'guide_dorm', 'num_freshmen',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Dorm.num_sophomores'
        db.add_column(u'guide_dorm', 'num_sophomores',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Deleting field 'Dorm.room_dimensions'
        db.delete_column(u'guide_dorm', 'room_dimensions')


        # Changing field 'Dorm.dist_to_bk'
        db.alter_column(u'guide_dorm', 'dist_to_bk', self.gf('django.db.models.fields.FloatField')(default=2))

        # Changing field 'Dorm.dist_to_norris'
        db.alter_column(u'guide_dorm', 'dist_to_norris', self.gf('django.db.models.fields.FloatField')(default=2))

        # Changing field 'Dorm.style'
        db.alter_column(u'guide_dorm', 'style', self.gf('django.db.models.fields.CharField')(default='hallway', max_length=10))

        # Changing field 'Dorm.dist_to_tech'
        db.alter_column(u'guide_dorm', 'dist_to_tech', self.gf('django.db.models.fields.FloatField')(default=2))

        # Changing field 'Dorm.dist_to_kresge'
        db.alter_column(u'guide_dorm', 'dist_to_kresge', self.gf('django.db.models.fields.FloatField')(default=2))

        # Changing field 'Dorm.campus_side'
        db.alter_column(u'guide_dorm', 'campus_side', self.gf('django.db.models.fields.CharField')(default='South', max_length=10))

        # Changing field 'Dorm.dorm_type'
        db.alter_column(u'guide_dorm', 'dorm_type', self.gf('django.db.models.fields.CharField')(default='Hall', max_length=40))

        # Changing field 'Dorm.cost'
        db.alter_column(u'guide_dorm', 'cost', self.gf('django.db.models.fields.FloatField')(default=2735))

        # Changing field 'Dorm.master'
        db.alter_column(u'guide_dorm', 'master', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Dorm.singles'
        db.alter_column(u'guide_dorm', 'singles', self.gf('django.db.models.fields.IntegerField')(default=40))

        # Changing field 'Dorm.address'
        db.alter_column(u'guide_dorm', 'address', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Dorm.doubles'
        db.alter_column(u'guide_dorm', 'doubles', self.gf('django.db.models.fields.IntegerField')(default=80))

        # Changing field 'Dorm.blurb'
        db.alter_column(u'guide_dorm', 'blurb', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Dorm.size'
        db.alter_column(u'guide_dorm', 'size', self.gf('django.db.models.fields.IntegerField')(default=120))

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
            'freshmen_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_ac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'open_gender': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'room_dimensions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'singles': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
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