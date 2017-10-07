import urllib
import urllib2
import json
import csv
import thread
import time

def RequestFuc(paraDic, urlStr):                #return dic
                if len(paraDic) > 0:
                                url_values = urllib.urlencode(paraDic)
                                full_url = urlStr + '?' + url_values
                else:
                                full_url = urlStr
                req = urllib2.Request(full_url)
                req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
                response = urllib2.urlopen(req, timeout=15)                
                res_str = response.read()
                res_dic = json.loads(res_str)
                return res_dic
                

def SingleThread(readfile, writefile):
                fr = open(readfile, 'r')
                fw = open(writefile, 'wb')
                csvReader = csv.reader(fr)
                csvWriter = csv.writer(fw)
                num = 0
                for row in csvReader:
                                num = num + 1
                                appid = row[0] #string
                                data = {}
                                data['key'] = 'E94CA461AD4E2C0C530173DD98477B88'
                                data['appid'] = appid
                                url = 'http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2'
                                try:
                                                res_dic = RequestFuc(data, url)
                                except urllib2.HTTPError, e:
                                                print str(e.code)+': appid = '+str(appid)
                                                continue
                                if len(res_dic['game']) == 0:
                                                gameName=gameVersion='NULL'
                                else:
                                                gameName=res_dic['game']['gameName']
                                                gameVersion=res_dic['game']['gameVersion']
                                csvWriter.writerow([appid, gameName, gameVersion])
                                fw.flush()
                                print readfile + ': '+ str(num) + '/4050'
                                time.sleep(1)
                                
                fr.close()
                fw.close()


'''
thread.start_new_thread(SingleThread, ('all_steam_appid01.csv','test01.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid02.csv','test02.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid03.csv','test03.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid04.csv','test04.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid05.csv','test05.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid06.csv','test06.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid07.csv','test07.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid08.csv','test08.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid09.csv','test09.csv'))
'''
thread.start_new_thread(SingleThread, ('all_steam_appid10.csv','test10.csv'))

