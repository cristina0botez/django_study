# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flavor'
        db.create_table(u'flavors_flavor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('scoops_remaining', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
        ))
        db.send_create_signal(u'flavors', ['Flavor'])


    def backwards(self, orm):
        # Deleting model 'Flavor'
        db.delete_table(u'flavors_flavor')


    models = {
        u'flavors.flavor': {
            'Meta': {'object_name': 'Flavor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scoops_remaining': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['flavors']