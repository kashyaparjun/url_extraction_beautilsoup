import urllib3
from bs4 import BeautifulSoup
url = "http://www.example.com"
http = urllib3.PoolManager()
request = http.request('GET', url)
a = request.data
ul = BeautifulSoup(a)
tmp = ul.findAll("a",href=True)
links = []
for t in tmp:
    links.append(t['href'])

print links