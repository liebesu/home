import re
from bs4 import BeautifulSoup
import requests

__author__ = 'admin'


url='http://www.xlpu.cc/html/43395.html'
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
thunder_urls=soup.find_all(href=re.compile("thunder:"))
for thunder_url in thunder_urls:
    print thunder_url.text
    print thunder_url.get('href')
