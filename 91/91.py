from bs4 import BeautifulSoup
import requests
import json
import re
url='http://www.91porn.com/v.php'

for i in range(1,3603):
    s=requests.session()
    headers={'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
    payloads={'next':'watch','page':i}
    r=s.get(url,data=json.dumps(payloads),headers=headers)
    soup=BeautifulSoup(r.content,"html5lib")
    alllist=soup.find_all(href=re.compile('http://www.91porn.com/view_video.php'))
    print len(alllist)
    for a in alllist:
        if a.get('title'):
            titletxt=a.get('title')
            hreftxt=a.get('href')
            c=open('all.txt','a')
            c.write(titletxt.encode('utf8')+'\n')
            c.write(hreftxt+'\n')
            c.close()


