from multiprocessing.pool import Pool
import os

__author__ = 'liebesu'
from bs4 import BeautifulSoup
import requests
__author__ = 'admin'

def get_word():
    domains=open('dic/newwords').readlines()
    try:
        pool=Pool(processes=2)
        pool.map(check_domain,domains)
        pool.close()
        pool.join()
    except Exception as e:
        print e
        pass

def check_domain(domain):
    url='http://panda.www.net.cn/cgi-bin/check.cgi?area_domain='+domain.replace('\n','')+'.com'
    print url
    user_agent={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    proxies={'http':'http://120.52.72.23:80'}
    r=requests.get(url,headers= user_agent,proxies=proxies)
    json= r.text
    print json

    #returncode=soup.find(<returncode>)
    if 'Domain name is available'in r.text and '200' in r.text:
        print domain
        a=open('yes','a')
        a.write(domain)
        a.close()
    elif '200' in r.text and 'Domain exists' in r.text:
        a=open('finish','a')
        a.write(domain)
        a.close()
    else:
        a=open('other','a')
        a.write(domain)
        a.close()
if __name__=="__main__":
    os.system('cat finish dic/words  |sort | uniq -u > dic/newwords')

    get_word()
