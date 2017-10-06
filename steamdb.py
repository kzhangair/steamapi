import urllib2
import urllib
from bs4 import BeautifulSoup
 
url = 'https://steamdb.info/apps/page1'
req = urllib2.Request(url)
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = urllib2.urlopen(req)
page = response.read()
soup = BeautifulSoup(page, 'lxml')
tbody = soup.find_all('tbody')[0]
for child in tbody.children
	print child.attrs['data-appid']
