import os
import re
import requests
import MySQLdb
from urlparse import urljoin
from bs4 import BeautifulSoup
import ConfigParser
from lib.common.constants import HOME_CRAWLER_ROOT
def db_insert():
    pass
def readconf():
    file_conf_path=os.path.join(HOME_CRAWLER_ROOT,"conf","movie.conf")
    rf=ConfigParser.ConfigParser()
    rf.read(file_conf_path)
    url=rf.get("movie","url")
    serch_word=rf.get("movie","serch_word")
    return url,serch_word
def get_info():
    url,serch_word=readconf()
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")   
    movie_lists=soup.find_all(href=re.compile(serch_word+r"/\d*.html"),limit=42)
    for movie_info in movie_lists:
        if len(movie_info.text)>8:
            page_url=urljoin(url,movie_info.get('href'))
            print page_url
            r=requests.get(page_url)
            print r.content
            soup=BeautifulSoup(r.content,"html.parser")
            movie_info=soup.find(value=re.compile('xzurl='))
            
            print movie_info.get('value')
            
            
def db_check():
    db = MySQLdb.connect(host='localhost', db='pd_update', user='root', passwd='polydata', port=3306,
                         charset='utf8')
    cursor = db.cursor()    
if __name__=="__main__":
    get_info()
    
    
    