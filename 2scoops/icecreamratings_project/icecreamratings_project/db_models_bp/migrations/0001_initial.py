# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Parent'
        db.create_table(u'db_models_bp_parent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('some_field', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'db_models_bp', ['Parent'])

        # Adding model 'ParentSubclasser'
        db.create_table(u'db_models_bp_parentsubclasser', (
            (u'parent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['db_models_bp.Parent'], unique=True, primary_key=True)),
            ('reason', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'db_models_bp', ['ParentSubclasser'])


    def backwards(self, orm):
        # Deleting model 'Parent'
        db.delete_table(u'db_models_bp_parent')

        # Deleting model 'ParentSubclasser'
        db.delete_table(u'db_models_bp_parentsubclasser')


    models = {
        u'db_models_bp.parent': {
            'Meta': {'object_name': 'Parent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'some_field': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'db_models_bp.parentsubclasser': {
            'Meta': {'object_name': 'ParentSubclasser', '_ormbases': [u'db_models_bp.Parent']},
            u'parent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db_models_bp.Parent']", 'unique': 'True', 'primary_key': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['db_models_bp']