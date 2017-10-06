
import urllib2
import urllib
import csv
from bs4 import BeautifulSoup
fo = open('all_steam_appid.csv', 'wb')
csvWriter = csv.writer(fo)

for pagenum in range(1, 955):
	url = 'https://steamdb.info/apps/page' + str(pagenum)
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
	response = urllib2.urlopen(req)
	page = response.read()
	soup = BeautifulSoup(page, 'lxml')
	tbody = soup.find_all('tbody')[0]
	for tr in tbody.find_all('tr', recursive=False):
		print tr.attrs['data-appid']
		csvWriter.writerow([tr.attrs['data-appid']])

fo.close()

