# Maildir Filter

This script scans all read and unread mail messages stored in Maidir format (http://en.wikipedia.org/wiki/Maildir).
If an email contains a custom 'X-Filter-Folder' header the script uses the value of this custom header to create
a subfolder in the mailbox (if it doesn't exist yet) and moves the message to that subfolder.

## Usage

	maildir_filter (path/to/Maildir/folder/of/mailbox)
	eg maildir_filter /home/example/imap/example.com/example/Maildir

## Limitation of the X-Filter-Folder value

The X-Filter-Folder value can only contain alphanumeric characters.