from ftplib import FTP
import requests
import time

__author__ = 'liebesu'
import time
home_ip="ip/work.html"
def get_home_ip():
    try:
        ISOTIMEFORMAT='%Y-%m-%d %X'
        get_time=time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        url='http://1212.ip138.com/ic.asp'
        r=requests.get(url)
        a=open(home_ip,"a")
        a.write(get_time)
        a.write(r.content)
        a.close()
        ftp=FTP('qxu1142060259.my3w.com')
        ftp.login(user='qxu1142060259',passwd='liebesu2015')
        ftp.cwd('htdocs')
        ftp.storbinary('STOR work.html', open(home_ip, 'rb'))
        ftp.quit()
    except:
        pass

if __name__=="__main__":
    for i in range(100000):
        get_home_ip()
        time.sleep(1800)

