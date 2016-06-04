import csv
import requests
from BeautifulSoup import BeautifulSoup

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
#             'Upgrade-Insecure-Requests':1}
    

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Host':'xueqiu.com',
                    'Upgrade-Insecure-Requests': 1,
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}
                    # 'Cookie':'s=2rfd15xt45; __utma=1.1446861734.1464484351.1464484351.1464484351.1; __utmb=1.1.10.1464484351; __utmc=1; __utmz=1.1464484351.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); webp=1; _sid=eW8ckI9yjHgIR6fQHFVDQ3DfBlBa6O; bid=06518b3a2bf1fd756abb42fd5d8d68da_iorwe6kz; xq_a_token=934f674c5167ef0a40bc92c387554e5b8d74a6f8; xq_r_token=ed5549c6fd48ab1fbe3f40b00a823b21dbd4f618; Hm_lvt_1db88642e346389874251b5a1eded6e3=1464167262,1464484373,1464484468,1464484475; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1464484731'}
stock = "SH600570"
result = requests.get("https://xueqiu.com/S/"+stock+"/follows", headers=headers)
# result = requests.get("https://xueqiu.com/",headers=headers)
# result = requests.get("https://segmentfault.com/t/python/blogs?page=1")
# result = requests.get("http://www.baidu.com")
print result
print result.text
soup = BeautifulSoup(str(result.content))
print soup.title.getText()[:4]
spans = soup.findAll('span')
print spans
for span in spans:
    if span.get('class') is None:
        w = span
        print w
print w.text.split("(")[1].split(")")[0]

# for i in raw:
#     print type(i)
# print type(raw.string)
# print raw.string
# print soup.body.span
# print number
# with open('xueqiu.csv', 'rb') as csvfile:
#     xueqiuwriter = csv.writer(csvfile, delimiter=' ',
#                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     xueqiuwriter.writerow()
                              
        
    



