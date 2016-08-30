import requests
import re
from bs4 import BeautifulSoup
from urlparse import urljoin
url='http://www.ygdy8.net/html/gndy/dyzz/index.html'
r=requests.get(url)
soup=BeautifulSoup(r.content,"html5lib")
lists=soup.find_all(href=re.compile("/html/gndy/dyzz/\d*"))
for list in lists:
    if len(list.get_text())>10:
        print list.get_text()
        href=list.get('href')
        href=urljoin(url, href)        
        r=requests.get(href)
        new_soup=BeautifulSoup(r.content,"html5lib")
        download_url=new_soup.find(href=re.compile("thunder:*"))
        print download_url.get('href')
        print download_url.get('thundertype thundertype')
    
    
    