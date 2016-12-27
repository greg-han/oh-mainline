# This file is part of OpenHatch.
# Copyright (C) 2009 OpenHatch, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from south.db import db
from django.db import models
from mysite.profile.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'TagTypes'
        db.create_table('profile_tagtypes', (
            ('id', models.AutoField(primary_key=True)),
            ('prefix', models.CharField(max_length=20)),
        ))
        db.send_create_signal('profile', ['TagTypes'])
        
        # Adding model 'Link_PersonToProjectRelationship_Tag'
        db.create_table('profile_link_persontoprojectrelationship_tag', (
            ('id', models.AutoField(primary_key=True)),
            ('tag', models.ForeignKey(orm.Tag)),
            ('person_to_project_relationship', models.ForeignKey(orm.PersonToProjectRelationship)),
            ('time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 19, 12, 5, 1, 54833))),
            ('source', models.CharField(max_length=200)),
        ))
        db.send_create_signal('profile', ['Link_PersonToProjectRelationship_Tag'])
        
        # Adding model 'Tag'
        db.create_table('profile_tag', (
            ('id', models.AutoField(primary_key=True)),
            ('text', models.CharField(max_length=50)),
            ('type', models.CharField(max_length=50)),
        ))
        db.send_create_signal('profile', ['Tag'])
        
        # Changing field 'Person.time_record_was_created'
        db.alter_column('profile_person', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 19, 12, 5, 0, 489277)))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'TagTypes'
        db.delete_table('profile_tagtypes')
        
        # Deleting model 'Link_PersonToProjectRelationship_Tag'
        db.delete_table('profile_link_persontoprojectrelationship_tag')
        
        # Deleting model 'Tag'
        db.delete_table('profile_tag')
        
        # Changing field 'Person.time_record_was_created'
        db.alter_column('profile_person', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 18, 21, 24, 12, 967616)))
        
    
    
    models = {
        'profile.person': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'last_polled': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_touched': ('models.DateTimeField', [], {}),
            'name': ('models.CharField', [], {'max_length': '200'}),
            'password_hash_md5': ('models.CharField', [], {'max_length': '200'}),
            'poll_on_next_web_view': ('models.BooleanField', [], {'default': 'True'}),
            'time_record_was_created': ('models.DateTimeField', [], {'default': 'datetime.datetime(2009, 6, 19, 12, 5, 1, 569217)'}),
            'username': ('models.CharField', [], {'max_length': '200'})
        },
        'profile.link_persontoprojectrelationship_tag': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'person_to_project_relationship': ('models.ForeignKey', ["orm['profile.PersonToProjectRelationship']"], {}),
            'source': ('models.CharField', [], {'max_length': '200'}),
            'tag': ('models.ForeignKey', ["orm['profile.Tag']"], {}),
            'time_record_was_created': ('models.DateTimeField', [], {'default': 'datetime.datetime(2009, 6, 19, 12, 5, 1, 149232)'})
        },
        'profile.tag': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'text': ('models.CharField', [], {'max_length': '50'}),
            'type': ('models.CharField', [], {'max_length': '50'})
        },
        'search.project': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'profile.tagtypes': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('models.CharField', [], {'max_length': '20'})
        },
        'profile.persontoprojectrelationship': {
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'man_months': ('models.PositiveIntegerField', [], {}),
            'person': ('models.ForeignKey', ["orm['profile.Person']"], {}),
            'person_role': ('models.CharField', [], {'max_length': '200'}),
            'primary_language': ('models.CharField', [], {'max_length': '200'}),
            'project': ('models.ForeignKey', ["orm['search.Project']"], {}),
            'source': ('models.CharField', [], {'max_length': '100'}),
            'tags': ('models.TextField', [], {}),
            'time_finish': ('models.DateTimeField', [], {}),
            'time_record_was_created': ('models.DateTimeField', [], {}),
            'time_start': ('models.DateTimeField', [], {}),
            'url': ('models.URLField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['profile']
