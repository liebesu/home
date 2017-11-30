import requests
from bs4 import BeautifulSoup
from urllib import urlretrieve

url='http://www.hdwan.net/page/1'
r=requests.get(url)
if r.status_code==200:

    soup=BeautifulSoup(r.content,"html5lib")
    list_movie=soup.find_all(class_="zoom")
    for movie in list_movie:
        if "720P" or "1080" or "DB-" in movie.title:
            print movie.title
            print movie.href
