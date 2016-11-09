from bs4 import BeautifulSoup
import requests
import os
import sys
import time

try:
    url = "https://freevpn.me/accounts"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.text
        soup = BeautifulSoup(data,'html5lib')
        plandiv = soup.find("div",{"class":"plan"})
        getdata = plandiv.findAll('li')
        gotip =  str(getdata[0].getText()).split(':')[1]
        gotuser = str(getdata[1].getText()).split(':')[1]
        gotpass = str(getdata[2].getText()).split(':')[1]
        print gotip + " - " + gotuser + " - " + gotpass
        if "win" in sys.platform:
            print "Disconnecting All VPN's"
            os.system("rasdial /disconnect")
            time.sleep(2)
            connectcmd = "rasdial 12345 "+gotuser+" "+gotpass+" /phone:"+gotip
            print connectcmd
            os.system(connectcmd)


except Exception, e:
    print e