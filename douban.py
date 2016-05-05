#coding=UTF-8
import re
from urlparse import urljoin
import requests
from bs4 import BeautifulSoup
import time
import MySQLdb
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
    time.sleep(5)
    r=requests.get(tagurl)
    soup=BeautifulSoup(r.text,"html.parser")
    books=soup.find_all(class_="subject-item")
    for book in books:
        if book.h2.a.string:
            try:
                book_name=book.h2.a.string.replace(" ","").replace("\n","")
            except:
                book_name=book.h2.a.string.encode('GBK','ignore').replace(" ","").replace("\n","")
            data=[]
            data.append(tag_name)
            data.append(book_name)
            insert_db(data)
    next=soup.find(class_="next")
    try:
        nexturl=next.a.get('href')
        list_book(tag_name,urljoin(url,nexturl))
    except:
        pass
def insert_db(data):
    db= MySQLdb.connect(db="book", user="root", passwd="polydata", host="localhost", port=3306,charset='utf8')
    cursor=db.cursor()
    try:
        #print data[0],data[1]
        insert_sql='insert into douban(category_title,title) VALUES ' \
               '("%s","%s") '%(data[0],data[1])
        cursor.execute(insert_sql)
        db.commit()
        cursor.close()
        db.close()

    except Exception as e:
        cursor.close()
        db.close()
        print e
        exit()



if __name__=="__main__":
    url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    categery(url)


