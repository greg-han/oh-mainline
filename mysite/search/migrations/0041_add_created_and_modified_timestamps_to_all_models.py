# This file is part of OpenHatch.
# Copyright (C) 2010 OpenHatch, Inc.
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
from mysite.search.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'BugAnswer.created_date'
        db.add_column('search_buganswer', 'created_date', orm['search.buganswer:created_date'])
        
        # Adding field 'ProjectInvolvementQuestion.created_date'
        db.add_column('search_projectinvolvementquestion', 'created_date', orm['search.projectinvolvementquestion:created_date'])
        
        # Adding field 'Bug.modified_date'
        db.add_column('search_bug', 'modified_date', orm['search.bug:modified_date'])
        
        # Adding field 'HitCountCache.created_date'
        db.add_column('search_hitcountcache', 'created_date', orm['search.hitcountcache:created_date'])
        
        # Adding field 'HitCountCache.modified_date'
        db.add_column('search_hitcountcache', 'modified_date', orm['search.hitcountcache:modified_date'])
        
        # Adding field 'Answer.modified_date'
        db.add_column('search_answer', 'modified_date', orm['search.answer:modified_date'])
        
        # Adding field 'Answer.created_date'
        db.add_column('search_answer', 'created_date', orm['search.answer:created_date'])
        
        # Adding field 'Bug.created_date'
        db.add_column('search_bug', 'created_date', orm['search.bug:created_date'])
        
        # Adding field 'ProjectInvolvementQuestion.modified_date'
        db.add_column('search_projectinvolvementquestion', 'modified_date', orm['search.projectinvolvementquestion:modified_date'])
        
        # Adding field 'Project.created_date'
        db.add_column('search_project', 'created_date', orm['search.project:created_date'])
        
        # Adding field 'Project.modified_date'
        db.add_column('search_project', 'modified_date', orm['search.project:modified_date'])
        
        # Adding field 'BugAnswer.modified_date'
        db.add_column('search_buganswer', 'modified_date', orm['search.buganswer:modified_date'])
        
        # Adding field 'Bug.as_appears_in_distribution'
        #db.add_column('search_bug', 'as_appears_in_distribution', orm['search.bug:as_appears_in_distribution'])
        
        # Changing field 'Bug.last_polled'
        # (to signature: django.db.models.fields.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0)))
        db.alter_column('search_bug', 'last_polled', orm['search.bug:last_polled'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'BugAnswer.created_date'
        db.delete_column('search_buganswer', 'created_date')
        
        # Deleting field 'ProjectInvolvementQuestion.created_date'
        db.delete_column('search_projectinvolvementquestion', 'created_date')
        
        # Deleting field 'Bug.modified_date'
        db.delete_column('search_bug', 'modified_date')
        
        # Deleting field 'HitCountCache.created_date'
        db.delete_column('search_hitcountcache', 'created_date')
        
        # Deleting field 'HitCountCache.modified_date'
        db.delete_column('search_hitcountcache', 'modified_date')
        
        # Deleting field 'Answer.modified_date'
        db.delete_column('search_answer', 'modified_date')
        
        # Deleting field 'Answer.created_date'
        db.delete_column('search_answer', 'created_date')
        
        # Deleting field 'Bug.created_date'
        db.delete_column('search_bug', 'created_date')
        
        # Deleting field 'ProjectInvolvementQuestion.modified_date'
        db.delete_column('search_projectinvolvementquestion', 'modified_date')
        
        # Deleting field 'Project.created_date'
        db.delete_column('search_project', 'created_date')
        
        # Deleting field 'Project.modified_date'
        db.delete_column('search_project', 'modified_date')
        
        # Deleting field 'BugAnswer.modified_date'
        db.delete_column('search_buganswer', 'modified_date')
        
        # Deleting field 'Bug.as_appears_in_distribution'
        db.delete_column('search_bug', 'as_appears_in_distribution')
        
        # Changing field 'Bug.last_polled'
        # (to signature: django.db.models.fields.DateTimeField())
        db.alter_column('search_bug', 'last_polled', orm['search.bug:last_polled'])
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'search.answer': {
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['search.Project']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': "orm['search.ProjectInvolvementQuestion']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'search.bug': {
            'as_appears_in_distribution': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'bize_size_tag_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'canonical_bug_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'concerns_just_documentation': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True', 'null': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'date_reported': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'good_for_newcomers': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'last_polled': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)'}),
            'last_touched': ('django.db.models.fields.DateTimeField', [], {}),
            'looks_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'null': 'True'}),
            'people_involved': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['search.Project']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'submitter_realname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'submitter_username': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'search.buganswer': {
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['search.Project']", 'null': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bug_answers'", 'to': "orm['search.ProjectInvolvementQuestion']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'search.hitcountcache': {
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'hashed_query': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'hit_count': ('django.db.models.fields.IntegerField', [], {}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'null': 'True'})
        },
        'search.project': {
            'cached_contributor_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'date_icon_was_fetched_from_ohloh': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'icon_for_profile': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'icon_for_search_result': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'icon_raw': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'icon_smaller_for_badge': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'icon_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'logo_contains_name': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'search.projectinvolvementquestion': {
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_bug_style': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True', 'null': 'True'}),
            'key_string': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }
    
    complete_apps = ['search']
