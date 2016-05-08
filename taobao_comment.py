import requests

__author__ = 'admin'
url='https://www.taobao.com/'
r=requests.get(url)
print r.status_code
print r.text