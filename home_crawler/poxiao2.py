from bs4 import BeautifulSoup
import requests

url="http://www.poxiao.com/movie/41989.html"

r=requests.get(url)
print r.content
