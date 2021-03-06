# -*- coding: utf-8 -*-
import os,csv
import re,time
import requests
import MySQLdb
import commands
from urlparse import urljoin
from bs4 import BeautifulSoup
import ConfigParser
from lib.common.constants import HOME_CRAWLER_ROOT,THIRD_ROOT
import chardet
from baidupcsapi import PCS

def db_insert():
    pass
def readconf():
    file_conf_path=os.path.join(HOME_CRAWLER_ROOT,"conf","movie.conf")
    rf=ConfigParser.ConfigParser()
    rf.read(file_conf_path)
    url=rf.get("movie","url")
    serch_word=rf.get("movie","serch_word")
    save_path=rf.get("save", "path")
    db_host=rf.get("mysql_database", "host")
    db_user=rf.get("mysql_database", "user")
    db_passwd=rf.get("mysql_database", "passwd")
    db_dbname=rf.get("mysql_database", "db")
    baiduname=rf.get("baiduyun", "username")
    baidupwd=rf.get("baiduyun", "password")
    return url,serch_word,save_path,db_host,db_user,db_passwd,db_dbname
def get_info():
    url,serch_word,save_path,db_host,db_user,db_passwd,db_dbname=readconf()
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")   
    movie_lists=soup.find_all(href=re.compile(serch_word+r"/\d*.html"),limit=42)
    for movie_info in movie_lists:
        if len(movie_info.text)>8:
            page_url=urljoin(url,movie_info.get('href'))
            movie_name=re.findall(".*《(.*)》.*",movie_info.text)
            r=requests.get(page_url)
            soup=BeautifulSoup(r.content,"html5lib")
            movie_de_infos=soup.find_all(value=re.compile('xzurl='))
            for movie_de_info in movie_de_infos:
                download_url=movie_de_info.get('value').replace("xzurl=","")
                #downloader(download_url,save_path)
            with open('poxiao.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile,dialect='excel')
                list_csv=[]
                print movie_info.text
                list_csv.append(movie_info.text)
                list_csv.append(page_url)
                list_csv.append(download_url)
                spamwriter.writerow(list_csv)
def db_check():
    db = MySQLdb.connect(host='localhost', db='pd_update', user='root', passwd='liebesu', port=3306,
                         charset='utf8')
    cursor = db.cursor()
    sql_check="select movie from movie where "
def downloader(url,path):
    xunlei_script=os.path.normpath(os.path.join(THIRD_ROOT,"xunlei","lixian_cli.py"))
    print path
    cmd="python "+xunlei_script+" download "+url+" --output-dir "+path
    print str(cmd)
    info=os.popen(cmd,'r').read()
    if "saved" in info:
        print url+"download finished"
        
    else:
        cmd="python "+xunlei_script+" download "+url+" --continue --output-dir "+path
        os.popen(cmd)
    

def baiduyun(baiduname,baidupwd):
    data=time.strftime('%Y%m%d', time.localtime(time.time()))
    pcs=PCS._login
    pcs=PCS.mkdir("/movie/%s"%data)


if __name__=="__main__":
    import sys  
    reload(sys)  
    sys.setdefaultencoding('utf8')       
    get_info()
    
    
    