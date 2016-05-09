import hashlib
import requests

__author__ = 'admin'

url='http://www.domain-api.com/api-get-time.html'
username='liushui522@qq.com'
pwd='8589934592'
r=requests.get(url)
vtime=r.text.replace('<?xml version="1.0" encoding="utf-8"?><interface><time>','').replace('</time></interface>','')
m=hashlib.md5()
m.update('8589934592')
pwd_md5=m.hexdigest()
check=hashlib.md5()
check.update(username+pwd_md5+vtime)
checksum=check.hexdigest()
print checksum

payload={'username':username,'vtime':vtime,'checksum':checksum}
query_url='http://www.domain-api.com/api-product-domain-query.html'
r=requests.post(query_url,params=payload)
print r.text
new_url='http://www.domain-api.com/api-product-domain-query.html?domain=hodreams.com'
r=requests.get(new_url)
print r.text