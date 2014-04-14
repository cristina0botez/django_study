# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field customers on 'Supplier'
        m2m_table_name = db.shorten_name(u'multi_table_inheritance_supplier_customers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('supplier', models.ForeignKey(orm[u'multi_table_inheritance.supplier'], null=False)),
            ('restaurant', models.ForeignKey(orm[u'multi_table_inheritance.restaurant'], null=False))
        ))
        db.create_unique(m2m_table_name, ['supplier_id', 'restaurant_id'])


    def backwards(self, orm):
        # Removing M2M table for field customers on 'Supplier'
        db.delete_table(db.shorten_name(u'multi_table_inheritance_supplier_customers'))


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
            'customers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['multi_table_inheritance.Restaurant']", 'symmetrical': 'False'}),
            u'place_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table_inheritance.Place']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['multi_table_inheritance']