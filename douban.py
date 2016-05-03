#coding=UTF-8
import re
from urlparse import urljoin
import requests
from bs4 import BeautifulSoup
import time

__author__ = 'liebesu'
url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
def categery(url):
    r=requests.get(url)
    print r.status_code
    soup=BeautifulSoup(r.text,"html.parser")
    tags=soup.find_all(class_="tag")
    for tag in tags:
        tagurl=urljoin(url,tag.get('href'))
        tag_name=tag.get_text()
        list_book(tag_name,tagurl)
def list_book(tag_name,tagurl):
    r=requests.get(tagurl)
    soup=BeautifulSoup(r.text,"html.parser")
    books=soup.find_all(class_="subject-item")
    for book in books:
        if book.h2.a.string:
            try:
                print book.h2.a.string.replace(" ","").replace("\n","")
            except:
                print book.h2.a.string.encode('GBK','ignore').replace(" ","").replace("\n","")
    next=soup.find(class_="next")
    if next.a:
        nexturl=next.a.get('href')
        list_book(tag_name,nexturl)
    else:
        pass
    time.sleep(60)

if __name__=="__main__":
    url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    categery(url)


