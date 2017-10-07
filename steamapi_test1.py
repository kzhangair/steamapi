import urllib
import urllib2
import json
import csv
#fo = open('test.csv','wb')
#csvWriter = csv.writer(fo)
#csvWriter.writerow(['appid', 'title', 'url', 'author', 'contents'])
'''
data = {}
data['appid'] = 451080
data['count'] = '3'
data['maxlength'] = '300'
data['format'] = 'json'
url_values = urllib.urlencode(data)
print url_values
url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002'
full_url = url + '?' + url_values
print full_url
'''

full_url = 'http://api.steampowered.com/ISteamApps/GetAppList/v2'
req = urllib2.Request(full_url)
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')

response = urllib2.urlopen(req)
res_str = response.read() #json (string type)
res_dic = json.loads(res_str) #convert json to python dic
'''
res_appnews = res_dic['appnews']
res_newsitems = res_appnews['newsitems'][0]
'''

apps = res_dic['applist']['apps'] # applist
print 'appnum: ' + str(len(apps))
print apps[0]['appid']
print apps[0]['name']




#csvWriter.writerow([res_appnews['appid'], res_newsitems['title'], res_newsitems['url'], res_newsitems['author'], res_newsitems['contents']])


#fo.close()

