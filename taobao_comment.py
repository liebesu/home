#coding:UTF-8
import requests

__author__ = 'admin'
def test1():
    header={'Referer':'https://www.taobao.com',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    url='https://rate.taobao.com/feedRateList.htm?auctionNumId=527102009499&userNumId=246418327&currentPageNum=1&pageSize=40&rateType=&orderType=sort_weight&showContent=1&attribute=&sku=&hasSku=false&folded=0&ua=066UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5OcktwTnNPdUxzS35CfSs%3D%7CU2xMHDJ7G2AHYg8hAS8XKgQkClY3UT1aJF5wJnA%3D%7CVGhXd1llXGdZZFhiW2RcaVVqXWBCfkF%2BRn9LdUp%2BRH9KdkN2THZYDg%3D%3D%7CVWldfS0TMwk3CSkWNhhsDSN1Iw%3D%3D%7CVmJCbEIU%7CV2lJGSQEORknGiICOw47AyMfIRohATsANRUpFywXNw0yB1EH%7CWGFcYUF8XGNDf0Z6WmRcZkZ8R2dZDw%3D%3D&_ksTS=1463017425921_1249&callback=jsonp_tbcrate_reviews_list'
    url='https://rate.taobao.com/feedRateList.htm?auctionNumId=527525039334&userNumId=367142366&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&showContent=1&attribute=&sku=&hasSku=false&folded=0&callback=jsonp_tbcrate_reviews_list'
    cookie={'v':'0', 'thw':'cn','cna':'Osm6D3jDRXYCATFB9MyzoDKI','cookie2':'1cf03d604570666062a27eaf51b4f346', 't':'3aec712fba5fb4607ef2d0035c791ff4', 'uc1':'cookie14=UoWxMkAwwQtw8Q%3D%4D', 'l':'An5-hE0K5/9cC4uVpW/NAh0DTp7Av0I5'}

    r=requests.get(url,headers=header,verify=True,cookies=cookie)
    print r.status_code
    print r.cookies
    print r.text
    a=open('test/taobao.html','w')
    a.write(r.content)
    a.close()
def test2():
    header={'Referer':'https://www.taobao.com',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    cookie={'v':'0', 'thw':'cn','cna':'Osm6D3jDRXYCATFB9MyzoDKI','cookie2':'1cf03d604570666062a27eaf51b4f346', 't':'3aec712fba5fb4607ef2d0035c791ff4', 'uc1':'cookie14=UoWxMkAwwQtw8Q%3D%3D', 'l':'An5-hE0K5/9cC4uVpW/NAh0DTp7Av0I5'}
    url='https://www.taobao.com'
    r=requests.get(url,headers=header,verify=True,cookies=cookie)
    print r.cookies
def test3():
    header={'Referer':'https://www.taobao.com',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    url='https://rate.taobao.com/feedRateList.htm?auctionNumId=527102009499&userNumId=246418327&currentPageNum=1&pageSize=40&rateType=&orderType=sort_weight&showContent=1&attribute=&sku=&hasSku=false&folded=0&ua=066UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5OcktwTnNPdUxzS35CfSs%3D%7CU2xMHDJ7G2AHYg8hAS8XKgQkClY3UT1aJF5wJnA%3D%7CVGhXd1llXGdZZFhiW2RcaVVqXWBCfkF%2BRn9LdUp%2BRH9KdkN2THZYDg%3D%3D%7CVWldfS0TMwk3CSkWNhhsDSN1Iw%3D%3D%7CVmJCbEIU%7CV2lJGSQEORknGiICOw47AyMfIRohATsANRUpFywXNw0yB1EH%7CWGFcYUF8XGNDf0Z6WmRcZkZ8R2dZDw%3D%3D&_ksTS=1463017425921_1249&callback=jsonp_tbcrate_reviews_list'
    cookie={'v':'0', 'thw':'cn','cna':'Osm6D3jDRXYCATFB9MyzoDKI','cookie2':'1cf03d604570666062a27eaf51b4f346', 't':'3aec712fba5fb4607ef2d0035c791ff4', 'uc1':'cookie14=UoWxMkAwwQtw8Q%3D%4D', 'l':'An5-hE0K5/9cC4uVpW/NAh0DTp7Av0I5'}

    url='https://item.taobao.com/item.htm?spm=a230r.1.14.23.Vt3MyB&id=527525039334&ns=1&abbucket=19#detail'
    r=requests.get(url,headers=header,cookies=cookie)
    a=open('test/taobao.html','w')
    a.write(r.content)
    a.close()
def shoturl():
    header={'Referer':'https://www.taobao.com',
       'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    url='https://rate.taobao.com/feedRateList.htm?auctionNumId=527102009499&userNumId=246418327&currentPageNum=1&pageSize=40&rateType=&orderType=sort_weight&showContent=1&attribute=&sku=&hasSku=false&folded=0&ua=066UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5OcktwTnNPdUxzS35CfSs%3D%7CU2xMHDJ7G2AHYg8hAS8XKgQkClY3UT1aJF5wJnA%3D%7CVGhXd1llXGdZZFhiW2RcaVVqXWBCfkF%2BRn9LdUp%2BRH9KdkN2THZYDg%3D%3D%7CVWldfS0TMwk3CSkWNhhsDSN1Iw%3D%3D%7CVmJCbEIU%7CV2lJGSQEORknGiICOw47AyMfIRohATsANRUpFywXNw0yB1EH%7CWGFcYUF8XGNDf0Z6WmRcZkZ8R2dZDw%3D%3D&_ksTS=1463017425921_1249&callback=jsonp_tbcrate_reviews_list'
    cookie={'v':'0', 'thw':'cn','cna':'Osm6D3jDRXYCATFB9MyzoDKI','cookie2':'1cf03d604570666062a27eaf51b4f346', 't':'3aec712fba5fb4607ef2d0035c791ff4', 'uc1':'cookie14=UoWxMkAwwQtw8Q%3D%4D', 'l':'An5-hE0K5/9cC4uVpW/NAh0DTp7Av0I5'}
    url='https://rate.taobao.com/feedRateList.htm?auctionNumId=527525039334&currentPageNum=3&pageSize=20&rateType=&orderType=sort_weight&showContent=1&attribute=&sku=&hasSku=false&folded=0&callback=jsonp_tbcrate_reviews_list'
    r=requests.get(url,headers=header,cookies=cookie)
    print r.content
if __name__=="__main__":
    shoturl()