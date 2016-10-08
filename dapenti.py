import requests
url='http://www.dapenti.com/blog/more.asp?name=xilei&id='
for i in range(100000,120000):
    new_url=url+str(i)
    r=requests.get(new_url)
    if "早餐奶" in r.content:
        print i
        