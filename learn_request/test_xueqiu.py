import csv
import requests
from BeautifulSoup import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}
stock = "SH600570"
# result = requests.get("https://xueqiu.com/S/SH600570"+stock)
result = requests.get("https://xueqiu.com/S/SH600570/follows",headers=headers)
# result = requests.get("https://segmentfault.com/t/python/blogs?page=1")
# result = requests.get("http://www.baidu.com")
print result
soup = BeautifulSoup(str(result.content))
print soup.title.getText()
# number = soup.find(id="followsCount")
w = "cc"
spans = soup.findAll('span')
for span in spans:
    if span.get('class') == None:
        w = span
print w.content

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
                              
        
    



