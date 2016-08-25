#coding:utf-8
import os
import re
import requests
import MySQLdb
from urlparse import urljoin
from bs4 import BeautifulSoup
import ConfigParser
from lib.common.constants import HOME_CRAWLER_ROOT,THIRD_ROOT
def db_insert():
    pass
def readconf():
    file_conf_path=os.path.join(HOME_CRAWLER_ROOT,"conf","movie.conf")
    rf=ConfigParser.ConfigParser()
    rf.read(file_conf_path)
    url=rf.get("movie","url")
    serch_word=rf.get("movie","serch_word")
    save_path=rf.get("save", "path")
    return url,serch_word,save_path
def get_info():
    url,serch_word,save_path=readconf()
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")   
    movie_lists=soup.find_all(href=re.compile(serch_word+r"/\d*.html"),limit=42)
    for movie_info in movie_lists:
        if len(movie_info.text)>8:
            page_url=urljoin(url,movie_info.get('href'))
            print page_url
            r=requests.get(page_url)
            soup=BeautifulSoup(r.content,"html5lib")
            movie_info=soup.find(value=re.compile('xzurl='))
            
            download_url=movie_info.get('value').replace("xzurl=","")
            downloader(download_url,save_path)      
def db_check():
    db = MySQLdb.connect(host='localhost', db='pd_update', user='root', passwd='polydata', port=3306,
                         charset='utf8')
    cursor = db.cursor()    
def downloader(url,path):
    xunlei_script=os.path.normpath(os.path.join(THIRD_ROOT,"xunlei-lixian-master","lixian_cli.py"))
    print url
    print path
    os.system("python "+xunlei_script+" download "+url+" "+path)
    
    
if __name__=="__main__":
    get_info()
    
    
    