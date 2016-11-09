import os,requests
import json
import commands
from bs4 import BeautifulSoup
url='https://www.getgreenjsq.me/index.php'

def login_greenvpn(username,passwd):
    s = requests.Session()
    r=s.get(url)
    print r.status_code
    if r.status_code==200:
        soup=BeautifulSoup(r.content,'html5lib')
        return_value=soup.find(attrs={"name":"return"})
        return_value=return_value['value']
        md5_value=soup.find(value='1')
        md5_value=md5_value['name']
        payload={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        data={'username':'','passwd':'','remember':'yes','Submit':'%E7%99%BB%E5%BD%95','option':'com_user','task':'login','return':str(return_value),str(md5_value):'1'}
        
        loginr=s.post(url,data=data)
        print loginr.status_code
        
        xianluurl='https://www.getgreenjsq.me/xianlu.html'
        xianlur=s.get(xianluurl)
        print xianlur.status_code
        soupxian=BeautifulSoup(xianlur.content,"html5lib")
        lists=soupxian.find_all("center")
        all=[list.string for list in lists]
        line=len(all)/5
        url1=[]
        pathtxt='vpn.txt'
        if os.path.exists(pathtxt):
            os.remove(pathtxt)
        for i in range(1,line):
            
            if "." in all[i*5+2]:
                url1.append(all[i*5+2])
                a=open('vpn.txt','a')
                a.write(all[i*5+2]+'\n')
                a.close                
        print len(url1)    
        print url1
        
        
        
        
def get_vpn_url():
    connectcmd='rasdial python username password /phone:uk3.igjsq.top'
    result=os.popen(connectcmd)
    output=result.read()
    print output
    print type(output)
    print str(output)
    if "验证" in output:
        print "1"
    else:
        print "2"
    
def conn_vpn():
    pass
if __name__=="__main__":
    #login_greenvpn()
    get_vpn_url()
    conn_vpn()