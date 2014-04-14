# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'multi_table_inheritance_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'multi_table_inheritance', ['Place'])

        # Adding model 'Restaurant'
        db.create_table(u'multi_table_inheritance_restaurant', (
            (u'place_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table_inheritance.Place'], unique=True, primary_key=True)),
            ('serves_hot_dogs', self.gf('django.db.models.fields.BooleanField')()),
            ('serves_pizza', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'multi_table_inheritance', ['Restaurant'])

        # Adding model 'Supplier'
        db.create_table(u'multi_table_inheritance_supplier', (
            (u'place_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table_inheritance.Place'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'multi_table_inheritance', ['Supplier'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'multi_table_inheritance_place')

        # Deleting model 'Restaurant'
        db.delete_table(u'multi_table_inheritance_restaurant')

        # Deleting model 'Supplier'
        db.delete_table(u'multi_table_inheritance_supplier')


    models = {
        u'multi_table_inheritance.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'multi_table_inheritance.restaurant': {
            'Meta': {'object_name': 'Restaurant', '_ormbases': [u'multi_table_inheritance.Place']},
            u'place_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table_inheritance.Place']", 'unique': 'True', 'primary_key': 'True'}),
            'serves_hot_dogs': ('django.db.models.fields.BooleanField', [], {}),
            'serves_pizza': ('django.db.models.fields.BooleanField', [], {})
        },
        u'multi_table_inheritance.supplier': {
            'Meta': {'object_name': 'Supplier', '_ormbases': [u'multi_table_inheritance.Place']},
            u'place_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table_inheritance.Place']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['multi_table_inheritance']