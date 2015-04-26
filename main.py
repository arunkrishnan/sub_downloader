#!/usr/bin/env python

'''
  sub_downloader
'''

import sys
import xmlrpclib

def main():
  
  imdb_id = '0482571' # For testing
  
  url    = 'http://api.opensubtitles.org/xml-rpc'
  agent  = 'OSTestUserAgent'
  server =  xmlrpclib.Server(url)
  token  =  server.LogIn('','','en',agent)['token']
  
  search_query = [{'imdbid':imdb_id,'sublanguageid':'eng'}]
  response = server.SearchSubtitles(token,search_query)
  
  print response['data'][0]['SubDownloadLink']
  
if "__main__" == __name__:
  main()