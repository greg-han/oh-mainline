/*
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
*/

// This is just like a Django fixture, i.e., data used in testing.

Fixtures = {};

Fixtures.json = {
    'totalBugCount': 10,
    'start': 1,
    'end': 10,
    'bugs': [
    {
        "pk": 1,
        "model": "search.bug",
        "fields": {
            "status": "New",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "solsTiCe",
            "description": "when i play a mp3 track, and seek to 0:00 with the play toolbar, then the counter is rolling and that's make me believe the track is playing, but no sound is played at all.\nit work",
            "title": "when i seek to 0:00 in a mp3 nothing is played",
            "importance": "Undecided",
            "people_involved": 1,
            "last_touched": "2008-11-23T00:00:00Z",
            "submitter_username": "solstice-dhiver",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/301310",
            "date_reported": "2008-11-23T00:00:00Z"
        }
    }, 
    {
        "pk": 2,
        "model": "search.bug",
        "fields": {
            "status": "New",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Alex P",
            "description": "On Archlinux, when using the MTP Device support, Exaile segfaults after\nattempting to connect.\n\nConsole outupt is as follows:\nPlugins 'MTP Device Manager' version '0.4.0' loaded su",
            "title": "MTP device plugin causes segfaults",
            "importance": "Undecided",
            "people_involved": 1,
            "last_touched": "2009-04-13T00:00:00Z",
            "submitter_username": "puterbaugh0",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/360471",
            "date_reported": "2009-04-13T00:00:00Z"
        }
    }, 
    {
        "pk": 3,
        "model": "search.bug",
        "fields": {
            "status": "Fix Committed",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Vladimir Kokarev",
            "description": "column's I select to display in playlist reset after exaile restart\nfor example I'd like to see Year column always enabled\nand if I enable it and restart exaile, it disappears\nCan ",
            "title": "columns preferences aren't saved across restarts of exaile",
            "importance": "High",
            "people_involved": 6,
            "last_touched": "2008-04-07T00:00:00Z",
            "submitter_username": "me-matrix47",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/199080",
            "date_reported": "2008-03-06T00:00:00Z"
        }
    }, 
    {
        "pk": 4,
        "model": "search.bug",
        "fields": {
            "status": "Confirmed",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Mathias Brodala",
            "description": "After CD playback and ejecting the disc, the tracks remain in the\nplaylist. It should be cleared instead since the playback obviously\nwon't be possible without the disc.\n",
            "title": "Playlist remains populated after ejecting CD",
            "importance": "Low",
            "people_involved": 1,
            "last_touched": "2008-04-09T00:00:00Z",
            "submitter_username": "mathbr",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/138287",
            "date_reported": "2007-09-08T00:00:00Z"
        }
    }, 
    {
        "pk": 5,
        "model": "search.bug",
        "fields": {
            "status": "New",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Sascha14532",
            "description": "location: /usr/lib/xulrunner-1.9.0.4/libxpcom.so \nbefore 3\nExaile 0.2.14\n-----------------------\n  ( /usr/lib/exaile/exaile.py @ 18):\n-----------------------\nTraceback (mos",
            "title": "OperationalError: no such table: db_version",
            "importance": "Undecided",
            "people_involved": 2,
            "last_touched": "2008-11-19T00:00:00Z",
            "submitter_username": "sascha14532",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/299469",
                                                                           "date_reported": "2008-11-18T00:00:00Z"
        }
    }, 
    {
        "pk": 6,
        "model": "search.bug",
        "fields": {
            "status": "New",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "warp",
            "description": "OSD cover image altogether is not refreshed, but in the exaile cover picture is refreshed too totally randomly... :-(\nEaxaile 0.2.14/Hardy 8.04.1\n",
            "title": "Album image",
            "importance": "Undecided",
            "people_involved": 1,
            "last_touched": "2008-11-09T00:00:00Z",
            "submitter_username": "mail-csordaslaszlo",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/295916",
            "date_reported": "2008-11-09T00:00:00Z"
        }
    }, 
    {
        "pk": 7,
        "model": "search.bug",
        "fields": {
            "status": "Confirmed",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Adam Olsen",
            "description": "The svn (currently 2.11svn) supports an equalizer; it would be nice if\nit could be embedded among the free space above the progress bar, next\nto the album info, in the theme 'Dexai",
            "title": "Feature Request: Theme",
            "importance": "Wishlist",
            "people_involved": 1,
            "last_touched": "2007-08-30T00:00:00Z",
            "submitter_username": "arolsen",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/136166",
            "date_reported": "2007-08-30T00:00:00Z"
        }
    }, 
    {
        "pk": 8,
        "model": "search.bug",
        "fields": {
            "status": "Incomplete",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "revolutio",
            "description": "Running Xubuntu and Exaile has been the most stable music player I've\nfound. I've been running it for about two weeks now with little\ncomplication except the following:\n\nA few tim",
            "title": "Ratings periodically and selectively reset",
            "importance": "High",
            "people_involved": 10,
            "last_touched": "2009-04-01T00:00:00Z",
            "submitter_username": "revolutio",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/147270",
            "date_reported": "2007-09-30T00:00:00Z"
        }
    }, 
    {
        "pk": 9,
        "model": "search.bug",
        "fields": {
            "status": "New",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Darren Naessens",
            "description": "Hey,\n\nExaile v0.2.11on Fedora 8\n\nSome segfault output :\n\nJan 24 21:33:38 bobble kernel: exaile[3281]: segfault at 00000012 eip 00000012 esp 094f5790 error 4\nJan 21 22:02:35 bobble ",
            "title": "exaile segfaulting with error 4 and 6",
            "importance": "Undecided",
            "people_involved": 2,
            "last_touched": "2008-01-25T00:00:00Z",
            "submitter_username": "dpnaessens",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/185773",
            "date_reported": "2008-01-24T00:00:00Z"
        }
    }, 
    {
        "pk": 10,
        "model": "search.bug",
        "fields": {
            "status": "Confirmed",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Adam Olsen",
            "description": "When deleting files, Ubuntu doesn't physically remove them, but instead\ncreates a \".Trash-username\" folder in the drive root (\"/media/sdb1\n/.Trash-username\", for instance). After s",
            "title": "Files from deleted folders are added to collection",
            "importance": "Low",
            "people_involved": 1,
            "last_touched": "2008-04-09T00:00:00Z",
            "submitter_username": "arolsen",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/136116",
            "date_reported": "2007-08-30T00:00:00Z"
        }
    },
    {
        "pk": 11,
        "model": "search.bug",
        "fields": {
            "status": "Confirmed",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Adam Olsen",
            "description": "When deleting files, Ubuntu doesn't physically remove them, but instead\ncreates a \".Trash-username\" folder in the drive root (\"/media/sdb1\n/.Trash-username\", for instance). After s",
            "title": "Files from deleted folders are added to collection",
            "importance": "Low",
            "people_involved": 1,
            "last_touched": "2008-04-09T00:00:00Z",
            "submitter_username": "arolsen",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/136116",
            "date_reported": "2007-08-30T00:00:00Z"
        }
    },
    {
        "pk": 12,
        "model": "search.bug",
        "fields": {
            "status": "Confirmed",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Adam Olsen",
            "description": "When deleting files, Ubuntu doesn't physically remove them, but instead\ncreates a \".Trash-username\" folder in the drive root (\"/media/sdb1\n/.Trash-username\", for instance). After s",
            "title": "Files from deleted folders are added to collection",
            "importance": "Low",
            "people_involved": 1,
            "last_touched": "2008-04-09T00:00:00Z",
            "submitter_username": "arolsen",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/136116",
            "date_reported": "2007-08-30T00:00:00Z"
        }
    },
    {
        "pk": 13,
        "model": "search.bug",
        "fields": {
            "status": "Confirmed",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Adam Olsen",
            "description": "When deleting files, Ubuntu doesn't physically remove them, but instead\ncreates a \".Trash-username\" folder in the drive root (\"/media/sdb1\n/.Trash-username\", for instance). After s",
            "title": "Files from deleted folders are added to collection",
            "importance": "Low",
            "people_involved": 1,
            "last_touched": "2008-04-09T00:00:00Z",
            "submitter_username": "arolsen",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/136116",
            "date_reported": "2007-08-30T00:00:00Z"
        }
    },
    {
        "pk": 14,
        "model": "search.bug",
        "fields": {
            "status": "Confirmed",
            "last_polled": "2009-06-05T00:00:00Z",
            "submitter_realname": "Adam Olsen",
            "description": "When deleting files, Ubuntu doesn't physically remove them, but instead\ncreates a \".Trash-username\" folder in the drive root (\"/media/sdb1\n/.Trash-username\", for instance). After s",
            "title": "Files from deleted folders are added to collection",
            "importance": "Low",
            "people_involved": 1,
            "last_touched": "2008-04-09T00:00:00Z",
            "submitter_username": "arolsen",
            "project": "Exaile",
            "good_for_newcomers": 0,
            "canonical_bug_link": "https://bugs.launchpad.net/bugs/136116",
            "date_reported": "2007-08-30T00:00:00Z"
        }
    }
    ]
};

Fixtures.jsonArray = [Fixtures.json];

// vim: set nowrap:
