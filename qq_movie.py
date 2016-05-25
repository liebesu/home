import random

import requests

url='http://v.qq.com/page/r/k/5/r0302c1qzk5.html'
headers={"Content-type": "application/x-www-form-urlencoded", "Accept": "application/json, text/javascript, */*, q=0.01", "Referer": url}
cookies={'ts_refer':'cn.bing.com/search','pt2gguin':'o0453131680', 'uin':'o0453131680', 'skey':'@Q4KopYerM', 'ptisp':'ctc', 'RK':'YJMOn/FGbt', 'luin':'o0453131680', 'lskey':'00010000ac0e26fc3b3b78339c467719d670a6b4433fca621dc2ecf2fcdf85ec666ad7153f745864783a76bb', 'ptcz':'355f7432e3723a38fcecada30ca99758c95e5ee608dfa0705430d0693e9f8e7d', 'login_remember':'qq', "ad_play_index":"51","ptag":"cn_bing_com|uc.side._vmanage","pgv_info":"ssid=s547541959","ts_last":"v.qq.com/u/videos/","pgv_pvid":"4839526260","o_cookie":"453131680","ts_uid":"7898268901","main_login":"qq","encuin":"e64bb43f6b355eeee370ba49c9e883e0|453131680","lw_nick":"Liebesu|453131680|http://q1.qlogo.cn/g?b=qq&k=eNVCW6wsVicuHHhdjKDDvpQ&s=40&t=1371455940|1","_qdda":"3-1.9ep67","_qddab":"3-21q2sp.iomewiw4"}
ipproxies=[ip for ip in open('ipproxy/ip-1.txt').readlines()]
ip_len=len(ipproxies)
for i in range(0,1000):
    r = requests.Session()
    rand_ip={"http":ipproxies[random.randint(0,ip_len)].replace("\n","")}
    print rand_ip
    re=r.get(url,proxies=rand_ip,timeout=5)
    print re.status_code
