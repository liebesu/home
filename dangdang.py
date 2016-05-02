#coding=UTF-8
from urlparse import urljoin
__author__ = 'liebesu'
import re
from bs4 import BeautifulSoup
import requests

def computer_book_category(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    categorys=soup.find_all(href=re.compile("category_path=01\.54"))
    for category in categorys:
        try:
            title=category.get_text()
            print title
        except:
            title=category.get_text().encode('GBK', 'ignore');
            print title
        category_title=title
        category_href=category.get('href')
        computer_books_info(category_title,category_href)
def computer_books_info(category_title,category_href):
    r=requests.get(category_href)
    soup=BeautifulSoup(r.text,"html.parser")


    books=soup.find_all(class_=re.compile("line\d"))
    for book in books:
        try:
            title=book.a['title']
            print title
        except:
            title=book.a['title'].encode('GBK','ignore')
            print title
        book_soup=BeautifulSoup(str(book),"html.parser")
        try:
            star=book_soup.find(class_="star").a.string
            print star
        except:
            star="not find star"
            print star
        try:
            author=book_soup.find(class_='author').a.string
            print author
        except:
            author="not find author"
            print author
        try:
            publishing_time=book_soup.find(class_='publishing_time').get_text()
            print publishing_time
        except:
            publishing_time="not find publishing time"
            print publishing_time
        try:
            publishing=book_soup.find(class_='publishing').get_text()
            print publishing
        except:
            publishing="not find publishing"
            print publishing
        try:
            price_n=book_soup.find(class_='price_n').get_text().encode('GBK','ignore')
            print price_n
        except:
            price_n="not find price_n"
            print price_n
        try:
            price_r=book_soup.find(class_='price_r').get_text().encode('GBK','ignore')
            print price_r
        except:
            price_r="not find price_r"
            print price_r
        a=open('cou1.txt','a')
        print category_title
        a.write("栏目："+category_title.encode('utf-8')+"\n")
        try:
            a.write("书名："+title.encode('utf-8')+"\n")
        except:
            a.write("书名："+title+"\n")
        a.write("评论数："+star.encode('utf-8')+"\n")
        a.write("作者："+author.encode('utf-8')+"\n")
        a.write("出版时间："+publishing_time.encode('utf-8')+"\n")
        a.write("出版社:"+publishing.encode('utf-8')+"\n")
        a.write("当当价格："+price_r.encode('utf-8')+"\n")
        a.write("书价："+price_n.encode('utf-8')+"\n")
        a.write("\n")
        a.close()
        data=[]
        data.append(category_title)
        data.append(title)
        data.append(star)
        data.append(author)
        data.append(publishing_time)
        data.append(publishing)
        data.append(price_r)
        data.append(price_n)

    try:
        cat_url='http://category.dangdang.com/'
        next_url=soup.find(class_="next").a.get('href')
        full_next_url=urljoin(cat_url,next_url)
        print category_title,full_next_url
        computer_books_info(category_title,full_next_url)
    except:
        pass





def insert_db():
    db= MySQLdb.connect(db="book", user="root", passwd="polydata", host="localhost", port=3306,charset='utf8')
    cursor=db.cursor()
    

    pass

if __name__=="__main__":
    url='http://book.dangdang.com/'
    computer_book_category(url)

