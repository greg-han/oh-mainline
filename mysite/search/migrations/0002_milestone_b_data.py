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
import datetime
from mysite.search.models import *

class Migration:
    def forwards(self, orm):
        
        try:
            # Adding field 'Bug.submitter_realname'
            db.add_column('search_bug', 'submitter_realname', models.CharField(max_length=200))
        except:
            pass

        try:
             # Adding field 'Project.icon_url'
            db.add_column('search_project', 'icon_url', models.URLField(max_length=200))
        except:
            pass
        
        try:
            # Adding field 'Bug.last_touched'
            db.add_column('search_bug', 'last_touched', models.DateField(default=datetime.datetime(1970, 1, 1, 12, 0, 0)))
        except:
            pass
        
        try:
            # Adding field 'Bug.importance'
            db.add_column('search_bug', 'importance', models.CharField(max_length=200))
        except:
            pass
        
        try:
            # Adding field 'Bug.people_involved'
            db.add_column('search_bug', 'people_involved', models.IntegerField(default=0))
        except:
            pass
        
        try:
            # Adding field 'Bug.last_polled'
            db.add_column('search_bug', 'last_polled', models.DateField(default=datetime.datetime(1970, 1, 1, 12, 0, 0)))
        except:
            pass
        
        try:
            # Adding field 'Bug.submitter_username'
            db.add_column('search_bug', 'submitter_username', models.CharField(max_length=200))
        except:
            pass
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Bug.submitter_realname'
        db.delete_column('search_bug', 'submitter_realname')
        
        # Deleting field 'Project.icon_url'
        db.delete_column('search_project', 'icon_url')
        
        # Deleting field 'Bug.last_touched'
        db.delete_column('search_bug', 'last_touched')
        
        # Deleting field 'Bug.importance'
        db.delete_column('search_bug', 'importance')
        
        # Deleting field 'Bug.people_involved'
        db.delete_column('search_bug', 'people_involved')
        
        # Deleting field 'Bug.last_polled'
        db.delete_column('search_bug', 'last_polled')
        
        # Deleting field 'Bug.submitter_username'
        db.delete_column('search_bug', 'submitter_username')
        
    
    
    models = {
        'search.project': {
            'icon_url': ('models.URLField', [], {'max_length': '200'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'language': ('models.CharField', [], {'max_length': '200'}),
            'name': ('models.CharField', [], {'max_length': '200'})
        },
        'search.bug': {
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'importance': ('models.CharField', [], {'max_length': '200'}),
            'last_polled': ('models.DateField', [], {}),
            'last_touched': ('models.DateField', [], {}),
            'people_involved': ('models.IntegerField', [], {}),
            'project': ('models.ForeignKey', ['Project'], {}),
            'status': ('models.CharField', [], {'max_length': '200'}),
            'submitter_realname': ('models.CharField', [], {'max_length': '200'}),
            'submitter_username': ('models.CharField', [], {'max_length': '200'}),
            'title': ('models.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['search']
