
import requests

url='http://pan.baidu.com/share/home?uk=3608297983#category/type=0'
s=requests.session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'})
r=requests.get(url)
print r.encoding
r.encoding = 'UTF-8'
print r.text