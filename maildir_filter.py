#!/usr/bin/env python

import os
import sys
import email
import re

if len(sys.argv) > 1:
    maildir = sys.argv[1]
else:
    maildir = os.getcwd()

cur_maildir_folder = os.path.join(maildir, 'cur')
new_maildir_folder = os.path.join(maildir, 'new')

if not os.path.isdir(cur_maildir_folder) and not os.path.isdir(new_maildir_folder):
    print 'This does not seem a valid Maildir folder. Please try again.'
    exit()

def readFolder(folder, subfolder):
    for file in os.listdir(folder):
	path = os.path.join(folder, file)
	if os.path.isfile(path):
	    f = open(path)
	    msg = email.message_from_file(f)
	    f.close()

	    parser = email.parser.HeaderParser()
	    headers = parser.parsestr(msg.as_string())

	    for h in headers.items():
		if (h[0] == 'X-Filter-Folder'):
		    filter_folder = re.sub(r'[^a-zA-Z0-9: ]', '', h[1])
		    if filter_folder:
			dest_folder = os.path.join(maildir, '.' + filter_folder)
			print dest_folder
			if not os.path.exists(dest_folder):
			    os.makedirs(dest_folder)
			    os.makedirs(os.path.join(dest_folder, 'cur'))
			    os.makedirs(os.path.join(dest_folder, 'new'))
			os.rename(path, os.path.join(dest_folder, subfolder, file))

readFolder(cur_maildir_folder, 'cur')
readFolder(new_maildir_folder, 'new')