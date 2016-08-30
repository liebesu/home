import requests
import re
from bs4 import BeautifulSoup
url='http://www.ygdy8.net/html/gndy/dyzz/index.html'
r=requests.get(url)
soup=BeautifulSoup(r.content,"html5lib")
lists=soup.find_all(href=re.compile("/html/gndy/dyzz/\d*"))
for list in lists:
    print list.get_text()
    print list.get('href')