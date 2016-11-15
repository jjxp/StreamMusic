#encoding:utf-8

import os
import re
import urllib2

from whoosh.fields import *
from whoosh.index import create_in
import sys

title = sys.argv[1]
artist = sys.argv[2]
album = sys.argv[3]
url = sys.argv[4]

def addSong(title=title,artist=artist,album=album,url=url):
	url = "https://www.youtubeinmp3.com/fetch/?format=text&video=" + url

	response = urllib2.urlopen(url)
	download_link = re.findall(r"Link: (.+)",response.read())[0]

	if not os.path.exists("files"):
		os.mkdir("files")
	if not os.path.exists("files/"+artist):
		os.mkdir("files/"+artist)
	if not os.path.exists("files/"+artist+"/"+album):
		os.mkdir("files/"+artist+"/"+album)

	mp3file = urllib2.urlopen(download_link)
	with open('./files/'+artist+'/'+album+'/'+title+'.mp3','wb') as output:
		output.write(mp3file.read())
		
	schema = Schema(title=KEYWORD(stored=True),artist=KEYWORD(stored=True),album=TEXT(stored=True))

	if not os.path.exists("index"):
		os.mkdir("index")
	ix = create_in("index", schema)

	writer = ix.writer()

	writer.add_document(title=unicode(title),artist=unicode(artist),album=unicode(album))

	writer.commit()

	print "Added: ["+title+".mp3]"
	
if __name__ == "__main__":
	addSong(title,artist,album,url)