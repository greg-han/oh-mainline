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
        
        # Adding field 'Link_Person_Tag.person'
        db.add_column('profile_link_person_tag', 'person', models.ForeignKey(orm.Person, null=True))
        
        # Deleting field 'Link_Person_Tag.project'
        db.delete_column('profile_link_person_tag', 'project_id')
        
        # Changing field 'Person.time_record_was_created'
        db.alter_column('profile_person', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 29, 0, 57, 6, 907059)))
        
        # Changing field 'Link_Person_Tag.time_record_was_created'
        db.alter_column('profile_link_person_tag', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 29, 0, 57, 7, 489492)))
        
        # Changing field 'Link_ProjectExp_Tag.time_record_was_created'
        db.alter_column('profile_link_projectexp_tag', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 29, 0, 57, 7, 310687)))
        
        # Changing field 'Link_Project_Tag.time_record_was_created'
        db.alter_column('profile_link_project_tag', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 29, 0, 57, 7, 405992)))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Link_Person_Tag.person'
        db.delete_column('profile_link_person_tag', 'person_id')
        
        # Adding field 'Link_Person_Tag.project'
        db.add_column('profile_link_person_tag', 'project', models.ForeignKey(orm['profile.Person']))
        
        # Changing field 'Person.time_record_was_created'
        db.alter_column('profile_person', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 29, 0, 21, 25, 501145)))
        
        # Changing field 'Link_Person_Tag.time_record_was_created'
        db.alter_column('profile_link_person_tag', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 29, 0, 21, 25, 346041)))
        
        # Changing field 'Link_ProjectExp_Tag.time_record_was_created'
        db.alter_column('profile_link_projectexp_tag', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 29, 0, 21, 25, 125823)))
        
        # Changing field 'Link_Project_Tag.time_record_was_created'
        db.alter_column('profile_link_project_tag', 'time_record_was_created', models.DateTimeField(default=datetime.datetime(2009, 6, 29, 0, 21, 25, 843354)))
        
    
    
    models = {
        'profile.person': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'interested_in_working_on': ('models.CharField', [], {'default': "''", 'max_length': '1024'}),
            'last_polled': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_touched': ('models.DateTimeField', [], {'null': 'True'}),
            'name': ('models.CharField', [], {'max_length': '200'}),
            'password_hash_md5': ('models.CharField', [], {'max_length': '200'}),
            'poll_on_next_web_view': ('models.BooleanField', [], {'default': 'True'}),
            'time_record_was_created': ('models.DateTimeField', [], {'default': 'datetime.datetime(2009, 6, 29, 0, 57, 8, 291705)'}),
            'username': ('models.CharField', [], {'max_length': '200'})
        },
        'profile.link_person_tag': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'person': ('models.ForeignKey', ["orm['profile.Person']"], {}),
            'source': ('models.CharField', [], {'max_length': '200'}),
            'tag': ('models.ForeignKey', ["orm['profile.Tag']"], {}),
            'time_record_was_created': ('models.DateTimeField', [], {'default': 'datetime.datetime(2009, 6, 29, 0, 57, 8, 129528)'})
        },
        'profile.tag': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'tag_type': ('models.ForeignKey', ["orm['profile.TagType']"], {}),
            'text': ('models.CharField', [], {'max_length': '50'})
        },
        'profile.link_projectexp_tag': {
            'Meta': {'unique_together': "[('tag','project_exp','source'),]"},
            'favorite': ('models.BooleanField', [], {'default': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'project_exp': ('models.ForeignKey', ["orm['profile.ProjectExp']"], {}),
            'source': ('models.CharField', [], {'max_length': '200'}),
            'tag': ('models.ForeignKey', ["orm['profile.Tag']"], {}),
            'time_record_was_created': ('models.DateTimeField', [], {'default': 'datetime.datetime(2009, 6, 29, 0, 57, 7, 903579)'})
        },
        'profile.sourceforgeperson': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'username': ('models.CharField', [], {'max_length': '200'})
        },
        'profile.link_project_tag': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'project': ('models.ForeignKey', ["orm['search.Project']"], {}),
            'source': ('models.CharField', [], {'max_length': '200'}),
            'tag': ('models.ForeignKey', ["orm['profile.Tag']"], {}),
            'time_record_was_created': ('models.DateTimeField', [], {'default': 'datetime.datetime(2009, 6, 29, 0, 57, 8, 643880)'})
        },
        'profile.sourceforgeproject': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'unixname': ('models.CharField', [], {'max_length': '200'})
        },
        'search.project': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'profile.link_sf_proj_dude_fm': {
            'Meta': {'unique_together': "[('person','project'),]"},
            'date_collected': ('models.DateTimeField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('models.BooleanField', [], {'default': 'False'}),
            'person': ('models.ForeignKey', ["orm['profile.SourceForgePerson']"], {}),
            'position': ('models.CharField', [], {'max_length': '200'}),
            'project': ('models.ForeignKey', ["orm['profile.SourceForgeProject']"], {})
        },
        'profile.tagtype': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'prefix': ('models.CharField', [], {'max_length': '20'})
        },
        'profile.projectexp': {
            'description': ('models.TextField', [], {}),
            'favorite': ('models.BooleanField', [], {'default': '0'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'last_touched': ('models.DateTimeField', [], {'null': 'True'}),
            'man_months': ('models.PositiveIntegerField', [], {'null': 'True'}),
            'person': ('models.ForeignKey', ["orm['profile.Person']"], {}),
            'person_role': ('models.CharField', [], {'max_length': '200'}),
            'primary_language': ('models.CharField', [], {'max_length': '200', 'null': 'True'}),
            'project': ('models.ForeignKey', ["orm['search.Project']"], {}),
            'source': ('models.CharField', [], {'max_length': '100', 'null': 'True'}),
            'time_record_was_created': ('models.DateTimeField', [], {'null': 'True'}),
            'url': ('models.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }
    
    complete_apps = ['profile']
