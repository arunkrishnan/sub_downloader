#!/usr/bin/env python

'''
  sub_downloader
'''

import sys
import xmlrpclib
import urllib2
import gzip
import tempfile
import shutil
import os

def main():
  
  imdb_id = '0482571' # For testing
  
  url    = 'http://api.opensubtitles.org/xml-rpc'
  agent  = 'OSTestUserAgent'
  server =  xmlrpclib.Server(url)
  token  =  server.LogIn('','','en',agent)['token']
  
  search_query = [{'imdbid':imdb_id,'sublanguageid':'eng'}]
  response = server.SearchSubtitles(token,search_query)
  
  sub_url = response['data'][0]['SubDownloadLink']
  
  zip_url = urllib2.urlopen(response['data'][0]['SubDownloadLink'])
  
  zip_contents = zip_url.read()
  zip_url.close()
  
  #fd = file('test','wb')
  #fd.write(zip_contents)
  #fd.close()
 
  #f = gzip.GzipFile('test','r')
  #f.close()
  
  #for line in f:
    #print line
    
  tempdir = tempfile.mkdtemp()
  try:
    basename = sub_url.split('/')[-1]
    tempfilename = os.path.join(tempdir, basename)
    with file(tempfilename, 'wb') as f:
      f.write(zip_contents)
    f = gzip.GzipFile(tempfilename, 'r')
    try:
      subtitle_contents = f.read()
    finally:
      f.close()
  
        # copy it over the new filename
    with file('test', 'w') as f:
      f.write(subtitle_contents)
  finally:
    shutil.rmtree(tempdir)

if "__main__" == __name__:
    main()