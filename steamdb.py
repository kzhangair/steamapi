import urllib2
import urllib

url = 'https://steamdb.info/apps/page1'
req = urllib2.Request(url)
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
