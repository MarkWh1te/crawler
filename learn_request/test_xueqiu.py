import requests
from BeautifulSoup import BeautifulSoup

page = 1
result = requests.get("https://segmentfault.com/t/python/blogs?page="+str(page))
# result = requests.get("https://segmentfault.com/t/python/blogs?page=1")
# result = requests.get("http://www.baidu.com")
soup = BeautifulSoup(str(result.content))
print soup.title





