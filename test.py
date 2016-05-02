#coding:UTF-8
import requests
from bs4 import BeautifulSoup
res = requests.get("http://search.dangdang.com/?key=u%C5%CC16g&act=input")
soup = BeautifulSoup(res.text)
a = soup.select(".con.shoplist")
for i in a[0].select('li'):
    print "商品名:",i.select(".pic")[0].attrs['title'].strip()
    print "价格:",i.select(".price_n")[0].text.strip()
    print "评论数量:",i.findAll(attrs={"name":"itemlist-review"})[0].text
    a=i.select(".price_n")[0].text.strip()
    print "---------------------------------------------------------"