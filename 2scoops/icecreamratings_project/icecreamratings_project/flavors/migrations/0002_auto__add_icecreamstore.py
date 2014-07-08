# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IceCreamStore'
        db.create_table(u'flavors_icecreamstore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('block_address', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'flavors', ['IceCreamStore'])


    def backwards(self, orm):
        # Deleting model 'IceCreamStore'
        db.delete_table(u'flavors_icecreamstore')


    models = {
        u'flavors.flavor': {
            'Meta': {'object_name': 'Flavor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scoops_remaining': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'flavors.icecreamstore': {
            'Meta': {'object_name': 'IceCreamStore'},
            'block_address': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['flavors']