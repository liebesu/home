
import requests
from bs4 import BeautifulSoup
from multiprocessing.pool import Pool

def get_name(id):
    url='http://pan.baidu.com/share/home'
    
    headers={'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    payload={'uk':str(id)}
    r=requests.get(url,params=payload,headers=headers)
    print r.encoding
    soup=BeautifulSoup(r.content,'html5lib')
    name=soup.find(class_='pic-frm-pic')
    a=open('a.txt','a')
    a.write(name.get('alt')+'/n')
    a.close
    

if __name__=="__main__":
    a=range(1,100000)
    pool=Pool(processes=10)
    pool.map(get_name, a)
    pool.close()
    pool.join()
    