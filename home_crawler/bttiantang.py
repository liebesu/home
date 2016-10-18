import requests
import os
from bs4 import BeautifulSoup
url='http://www.bttiantang99.com/'

def get_info():
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html5lib')
    soup.findAll(class_='post box row fixed-hight')

if __name__=='__main__':
    get_info()