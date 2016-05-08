import os
import re
import requests
__author__ = 'admin'
global count
def get_word():
    for domain in open('dic/newwords').readlines():
        try:
            check_domain(domain)
        except Exception as e:
            print e
            pass

def check_domain(domain):
    url='http://www.yumingco.com/api/'
    payload={'domain':domain,'suffix':'com'
    }
    r=requests.get(url,params=payload)
    json= r.json()
    print json['status']
    if json['status'] and json['available']:
        print domain
        a=open('yes','a')
        a.write(domain)
        a.close()
    elif json['status'] :
        a=open('finish','a')
        a.write(domain+'\n')
        a.close()
if __name__=="__main__":
    #os.system('cat finish dic/words  |sort | uniq -u > dic/newwords')
    count=0
    get_word()