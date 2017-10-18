# -*- coding:utf-8 -*-
import urllib
import urllib2
import json
import csv
import thread
import time
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
def RequestFuc(paraDic, urlStr):                #return dic
                if len(paraDic) > 0:
                                url_values = urllib.urlencode(paraDic)
                                full_url = urlStr + '?' + url_values
                else:
                                full_url = urlStr
                req = urllib2.Request(full_url)
                req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
                response = urllib2.urlopen(req, timeout=20)                
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
                                print readfile + ': '+ str(num) + '/4050'
                                appid = row[0] #string
                                #############GetSchemaForGame#################
                                #gameName, gameVersion
                                data = {}
                                data['key'] = 'E94CA461AD4E2C0C530173DD98477B88'
                                data['appid'] = appid
                                data['format'] = json
                                url = 'http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2'
                                try:
                                                res_dic = RequestFuc(data, url)
                                except urllib2.HTTPError, e:
                                                print str(e.code)+': appid = '+str(appid)
                                                continue
                                except urllib2.URLError, e:
                                                continue
                                if len(res_dic['game']) == 0:
                                                gameName=gameVersion='NULL'
                                else:
                                                gameName=res_dic['game']['gameName']
                                                gameVersion=res_dic['game']['gameVersion']
                                #############GetNumberOfCurrentPlayers#################
                                #player_count
                                data = {}
                                data['appid'] = appid
                                data['format'] = json
                                url = 'http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1'
                                try:
                                                res_dic = RequestFuc(data, url)
                                except urllib2.HTTPError, e:
                                                print str(e.code)+': appid = '+str(appid)
                                                continue
                                except urllib2.URLError, e:
                                                continue
                                if len(res_dic) or len(res_dic['response']) == 0:
                                                player_count = 0
                                else:
                                                player_count = res_dic['response']['player_count']
                                
                                #############GetGlobalAchievementPercentagesForApp#################
                                data = {}
                                data['gameid'] = appid
                                data['format'] = json
                                url = 'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002'
                                try:
                                                res_dic = RequestFuc(data, url)
                                except urllib2.HTTPError, e:
                                                print str(e.code)+': appid = '+str(appid)
                                                continue
                                except urllib2.URLError, e:
                                                continue
                                achievements = [{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ,{'name':'defaut', 'percent':'0'}
                                                ]
                                if len(res_dic)>0 and len(res_dic['achievementpercentages']) > 0:
                                                if len(res_dic['achievementpercentages']['achievements']) > 10:
                                                                achievements = res_dic['achievementpercentages']['achievements'][0:10]
                                                else:
                                                                for i in range(len(res_dic['achievementpercentages']['achievements'])):
                                                                                achievements[i] = res_dic['achievementpercentages']['achievements'][i]
                                
                                #############GetGlobalAchievementPercentagesForApp#################
                                data = {}
                                data['appid'] = appid
                                data['format'] = json
                                url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002'
                                try:
                                                res_dic = RequestFuc(data, url)
                                except urllib2.HTTPError, e:
                                                print str(e.code)+': appid = '+str(appid)
                                                continue
                                except urllib2.URLError, e:
                                                continue
                                newsitems = [{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                             ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                                                                          ,{"gid": "3136051487782676067",
                                                "title": "Death To The Author: killing creators in Dishonored, Portal and BioShock",
                                                "url": "http://store.steampowered.com/news/externalpost/rps/3136051487782676067",
                                                "is_external_url": 'true',
                                                "author": "contact@rockpapershotgun.com (Hazel Monforton)",
                                                "contents": "<p><img src=\"https://assets.rockpapershotgun.com/images//2017/09/dishonoreddeath-620x329.jpg\" alt=\"dishonoreddeath\" width=\"620\" height=\"329\" class=\"alignnone size-medium wp-image-478303\" /></p>\n<p><em>When we meet the creators of fictional worlds, we often want to kill them. Whether its <a href=\"https://www.rockpapershotgun.com/tag/bioshock/\">Bioshock&#8217;s</a> Andrew Ryan and his deadly Rapture, GlaDOS and the sadistic test chambers of <a href=\"https://www.rockpapershotgun.com/tag/portal/\">Portal</a>, or <a href=\"https://www.rockpapershotgun.com/tag/dishonored-2/\">Kirin Jindosh and the Clockwork Mansion</a>. The urge to destroy these builders is partly down to the nature of their constructions &#8211; deathtraps and mazes that make the architect a cruel overseer &#8211; but there is perhaps more to it than that. With spoilers for the above, Hazel Monforton investigates the role (and the death) of the author in a medium that invites the audience into the action.</em></p>\n<p> <a href=\"https://www.rockpapershotgun.com/2017/09/19/death-of-creators-dishonored-portal-bioshock/#more-478267\" class=\"more-link\">(more&hellip;)</a></p>\n",
                                                "feedlabel": "Rock, Paper, Shotgun",
                                                "date": 1505844020,
                                                "feedname": "rps",
                                                "feed_type": 0,
                                                "appid": 620}
                                             ]
                                #newsitems
                                if len(res_dic) > 0 and len(res_dic['appnews']) > 0:
                                                if(len(res_dic['appnews']['newsitems']) > 20):
                                                                newsitems = res_dic['appnews']['newsitems'][0:20]
                                                else:
                                                                for i in range(0,len(res_dic['appnews']['newsitems'])):
                                                                               newsitems[i] = res_dic['appnews']['newsitems'][i]
                                                
                                                                                        
                                
                                  
                                csvWriter.writerow([appid, gameName, gameVersion, player_count,
                                                    achievements[0]['name'],achievements[0]['percent']
                                                    ,achievements[1]['name'],achievements[1]['percent']
                                                    ,achievements[2]['name'],achievements[2]['percent']
                                                    ,achievements[3]['name'],achievements[3]['percent']
                                                    ,achievements[4]['name'],achievements[4]['percent']
                                                    ,achievements[5]['name'],achievements[5]['percent']
                                                    ,achievements[6]['name'],achievements[6]['percent']
                                                    ,achievements[7]['name'],achievements[7]['percent']
                                                    ,achievements[8]['name'],achievements[8]['percent']
                                                    ,achievements[9]['name'],achievements[9]['percent']
                                                    ,newsitems[0]['gid'],newsitems[0]['title'],newsitems[0]['url'],newsitems[0]['author'],newsitems[0]['contents'],newsitems[0]['date']
                                                    ,newsitems[1]['gid'],newsitems[1]['title'],newsitems[1]['url'],newsitems[1]['author'],newsitems[1]['contents'],newsitems[1]['date']
                                                    ,newsitems[2]['gid'],newsitems[2]['title'],newsitems[2]['url'],newsitems[2]['author'],newsitems[2]['contents'],newsitems[2]['date']
                                                    ,newsitems[3]['gid'],newsitems[3]['title'],newsitems[3]['url'],newsitems[3]['author'],newsitems[3]['contents'],newsitems[3]['date']
                                                    ,newsitems[4]['gid'],newsitems[4]['title'],newsitems[4]['url'],newsitems[4]['author'],newsitems[4]['contents'],newsitems[4]['date']
                                                    ,newsitems[5]['gid'],newsitems[5]['title'],newsitems[5]['url'],newsitems[5]['author'],newsitems[5]['contents'],newsitems[5]['date']
                                                    ,newsitems[6]['gid'],newsitems[6]['title'],newsitems[6]['url'],newsitems[6]['author'],newsitems[6]['contents'],newsitems[6]['date']
                                                    ,newsitems[7]['gid'],newsitems[7]['title'],newsitems[7]['url'],newsitems[7]['author'],newsitems[7]['contents'],newsitems[7]['date']
                                                    ,newsitems[8]['gid'],newsitems[8]['title'],newsitems[8]['url'],newsitems[8]['author'],newsitems[8]['contents'],newsitems[8]['date']
                                                    ,newsitems[9]['gid'],newsitems[9]['title'],newsitems[9]['url'],newsitems[9]['author'],newsitems[9]['contents'],newsitems[9]['date']
                                                    ,newsitems[10]['gid'],newsitems[10]['title'],newsitems[10]['url'],newsitems[10]['author'],newsitems[10]['contents'],newsitems[10]['date']
                                                    ,newsitems[11]['gid'],newsitems[11]['title'],newsitems[11]['url'],newsitems[11]['author'],newsitems[11]['contents'],newsitems[11]['date']
                                                    ,newsitems[12]['gid'],newsitems[12]['title'],newsitems[12]['url'],newsitems[12]['author'],newsitems[12]['contents'],newsitems[12]['date']
                                                    ,newsitems[13]['gid'],newsitems[13]['title'],newsitems[13]['url'],newsitems[13]['author'],newsitems[13]['contents'],newsitems[13]['date']
                                                    ,newsitems[14]['gid'],newsitems[14]['title'],newsitems[14]['url'],newsitems[14]['author'],newsitems[14]['contents'],newsitems[14]['date']
                                                    ,newsitems[15]['gid'],newsitems[15]['title'],newsitems[15]['url'],newsitems[15]['author'],newsitems[15]['contents'],newsitems[15]['date']
                                                    ,newsitems[16]['gid'],newsitems[16]['title'],newsitems[16]['url'],newsitems[16]['author'],newsitems[16]['contents'],newsitems[16]['date']
                                                    ,newsitems[17]['gid'],newsitems[17]['title'],newsitems[17]['url'],newsitems[17]['author'],newsitems[17]['contents'],newsitems[17]['date']
                                                    ,newsitems[18]['gid'],newsitems[18]['title'],newsitems[18]['url'],newsitems[18]['author'],newsitems[18]['contents'],newsitems[18]['date']
                                                    ,newsitems[19]['gid'],newsitems[19]['title'],newsitems[19]['url'],newsitems[19]['author'],newsitems[19]['contents'],newsitems[19]['date']
                                                    ,appid, gameName, gameVersion, player_count,
                                                    achievements[0]['name'],achievements[0]['percent']
                                                    ,achievements[1]['name'],achievements[1]['percent']
                                                    ,achievements[2]['name'],achievements[2]['percent']
                                                    ,achievements[3]['name'],achievements[3]['percent']
                                                    ,achievements[4]['name'],achievements[4]['percent']
                                                    ,achievements[5]['name'],achievements[5]['percent']
                                                    ,achievements[6]['name'],achievements[6]['percent']
                                                    ,achievements[7]['name'],achievements[7]['percent']
                                                    ,achievements[8]['name'],achievements[8]['percent']
                                                    ,achievements[9]['name'],achievements[9]['percent']
                                                    ,newsitems[0]['gid'],newsitems[0]['title'],newsitems[0]['url'],newsitems[0]['author'],newsitems[0]['contents'],newsitems[0]['date']
                                                    ,newsitems[1]['gid'],newsitems[1]['title'],newsitems[1]['url'],newsitems[1]['author'],newsitems[1]['contents'],newsitems[1]['date']
                                                    ,newsitems[2]['gid'],newsitems[2]['title'],newsitems[2]['url'],newsitems[2]['author'],newsitems[2]['contents'],newsitems[2]['date']
                                                    ,newsitems[3]['gid'],newsitems[3]['title'],newsitems[3]['url'],newsitems[3]['author'],newsitems[3]['contents'],newsitems[3]['date']
                                                    ,newsitems[4]['gid'],newsitems[4]['title'],newsitems[4]['url'],newsitems[4]['author'],newsitems[4]['contents'],newsitems[4]['date']
                                                    ,newsitems[5]['gid'],newsitems[5]['title'],newsitems[5]['url'],newsitems[5]['author'],newsitems[5]['contents'],newsitems[5]['date']
                                                    ,newsitems[6]['gid'],newsitems[6]['title'],newsitems[6]['url'],newsitems[6]['author'],newsitems[6]['contents'],newsitems[6]['date']
                                                    ,newsitems[7]['gid'],newsitems[7]['title'],newsitems[7]['url'],newsitems[7]['author'],newsitems[7]['contents'],newsitems[7]['date']
                                                    ,newsitems[8]['gid'],newsitems[8]['title'],newsitems[8]['url'],newsitems[8]['author'],newsitems[8]['contents'],newsitems[8]['date']
                                                    ,newsitems[9]['gid'],newsitems[9]['title'],newsitems[9]['url'],newsitems[9]['author'],newsitems[9]['contents'],newsitems[9]['date']
                                                    ,newsitems[10]['gid'],newsitems[10]['title'],newsitems[10]['url'],newsitems[10]['author'],newsitems[10]['contents'],newsitems[10]['date']
                                                    ,newsitems[11]['gid'],newsitems[11]['title'],newsitems[11]['url'],newsitems[11]['author'],newsitems[11]['contents'],newsitems[11]['date']
                                                    ,newsitems[12]['gid'],newsitems[12]['title'],newsitems[12]['url'],newsitems[12]['author'],newsitems[12]['contents'],newsitems[12]['date']
                                                    ,newsitems[13]['gid'],newsitems[13]['title'],newsitems[13]['url'],newsitems[13]['author'],newsitems[13]['contents'],newsitems[13]['date']
                                                    ,newsitems[14]['gid'],newsitems[14]['title'],newsitems[14]['url'],newsitems[14]['author'],newsitems[14]['contents'],newsitems[14]['date']
                                                    ,newsitems[15]['gid'],newsitems[15]['title'],newsitems[15]['url'],newsitems[15]['author'],newsitems[15]['contents'],newsitems[15]['date']
                                                    ,newsitems[16]['gid'],newsitems[16]['title'],newsitems[16]['url'],newsitems[16]['author'],newsitems[16]['contents'],newsitems[16]['date']
                                                    ,newsitems[17]['gid'],newsitems[17]['title'],newsitems[17]['url'],newsitems[17]['author'],newsitems[17]['contents'],newsitems[17]['date']
                                                    ,newsitems[18]['gid'],newsitems[18]['title'],newsitems[18]['url'],newsitems[18]['author'],newsitems[18]['contents'],newsitems[18]['date']
                                                    ,newsitems[19]['gid'],newsitems[19]['title'],newsitems[19]['url'],newsitems[19]['author'],newsitems[19]['contents'],newsitems[19]['date']
                                                    ,appid, gameName, gameVersion, player_count,
                                                    achievements[0]['name'],achievements[0]['percent']
                                                    ,achievements[1]['name'],achievements[1]['percent']
                                                    ,achievements[2]['name'],achievements[2]['percent']
                                                    ,achievements[3]['name'],achievements[3]['percent']
                                                    ,achievements[4]['name'],achievements[4]['percent']
                                                    ,achievements[5]['name'],achievements[5]['percent']
                                                    ,achievements[6]['name'],achievements[6]['percent']
                                                    ,achievements[7]['name'],achievements[7]['percent']
                                                    ,achievements[8]['name'],achievements[8]['percent']
                                                    ,achievements[9]['name'],achievements[9]['percent']
                                                    ,newsitems[0]['gid'],newsitems[0]['title'],newsitems[0]['url'],newsitems[0]['author'],newsitems[0]['contents'],newsitems[0]['date']
                                                    ,newsitems[1]['gid'],newsitems[1]['title'],newsitems[1]['url'],newsitems[1]['author'],newsitems[1]['contents'],newsitems[1]['date']
                                                    ,newsitems[2]['gid'],newsitems[2]['title'],newsitems[2]['url'],newsitems[2]['author'],newsitems[2]['contents'],newsitems[2]['date']
                                                    ,newsitems[3]['gid'],newsitems[3]['title'],newsitems[3]['url'],newsitems[3]['author'],newsitems[3]['contents'],newsitems[3]['date']
                                                    ,newsitems[4]['gid'],newsitems[4]['title'],newsitems[4]['url'],newsitems[4]['author'],newsitems[4]['contents'],newsitems[4]['date']
                                                    ,newsitems[5]['gid'],newsitems[5]['title'],newsitems[5]['url'],newsitems[5]['author'],newsitems[5]['contents'],newsitems[5]['date']
                                                    ,newsitems[6]['gid'],newsitems[6]['title'],newsitems[6]['url'],newsitems[6]['author'],newsitems[6]['contents'],newsitems[6]['date']
                                                    ,newsitems[7]['gid'],newsitems[7]['title'],newsitems[7]['url'],newsitems[7]['author'],newsitems[7]['contents'],newsitems[7]['date']
                                                    ,newsitems[8]['gid'],newsitems[8]['title'],newsitems[8]['url'],newsitems[8]['author'],newsitems[8]['contents'],newsitems[8]['date']
                                                    ,newsitems[9]['gid'],newsitems[9]['title'],newsitems[9]['url'],newsitems[9]['author'],newsitems[9]['contents'],newsitems[9]['date']
                                                    ,newsitems[10]['gid'],newsitems[10]['title'],newsitems[10]['url'],newsitems[10]['author'],newsitems[10]['contents'],newsitems[10]['date']
                                                    ,newsitems[11]['gid'],newsitems[11]['title'],newsitems[11]['url'],newsitems[11]['author'],newsitems[11]['contents'],newsitems[11]['date']
                                                    ,newsitems[12]['gid'],newsitems[12]['title'],newsitems[12]['url'],newsitems[12]['author'],newsitems[12]['contents'],newsitems[12]['date']
                                                    ,newsitems[13]['gid'],newsitems[13]['title'],newsitems[13]['url'],newsitems[13]['author'],newsitems[13]['contents'],newsitems[13]['date']
                                                    ,newsitems[14]['gid'],newsitems[14]['title'],newsitems[14]['url'],newsitems[14]['author'],newsitems[14]['contents'],newsitems[14]['date']
                                                    ,newsitems[15]['gid'],newsitems[15]['title'],newsitems[15]['url'],newsitems[15]['author'],newsitems[15]['contents'],newsitems[15]['date']
                                                    ,newsitems[16]['gid'],newsitems[16]['title'],newsitems[16]['url'],newsitems[16]['author'],newsitems[16]['contents'],newsitems[16]['date']
                                                    ,newsitems[17]['gid'],newsitems[17]['title'],newsitems[17]['url'],newsitems[17]['author'],newsitems[17]['contents'],newsitems[17]['date']
                                                    ,newsitems[18]['gid'],newsitems[18]['title'],newsitems[18]['url'],newsitems[18]['author'],newsitems[18]['contents'],newsitems[18]['date']
                                                    ,newsitems[19]['gid'],newsitems[19]['title'],newsitems[19]['url'],newsitems[19]['author'],newsitems[19]['contents'],newsitems[19]['date']
                                                    ,appid, gameName, gameVersion, player_count,
                                                    achievements[0]['name'],achievements[0]['percent']
                                                    ,achievements[1]['name'],achievements[1]['percent']
                                                    ,achievements[2]['name'],achievements[2]['percent']
                                                    ,achievements[3]['name'],achievements[3]['percent']
                                                    ,achievements[4]['name'],achievements[4]['percent']
                                                    ,achievements[5]['name'],achievements[5]['percent']
                                                    ,achievements[6]['name'],achievements[6]['percent']
                                                    ,achievements[7]['name'],achievements[7]['percent']
                                                    ,achievements[8]['name'],achievements[8]['percent']
                                                    ,achievements[9]['name'],achievements[9]['percent']
                                                    ,newsitems[0]['gid'],newsitems[0]['title'],newsitems[0]['url'],newsitems[0]['author'],newsitems[0]['contents'],newsitems[0]['date']
                                                    ,newsitems[1]['gid'],newsitems[1]['title'],newsitems[1]['url'],newsitems[1]['author'],newsitems[1]['contents'],newsitems[1]['date']
                                                    ,newsitems[2]['gid'],newsitems[2]['title'],newsitems[2]['url'],newsitems[2]['author'],newsitems[2]['contents'],newsitems[2]['date']
                                                    ,newsitems[3]['gid'],newsitems[3]['title'],newsitems[3]['url'],newsitems[3]['author'],newsitems[3]['contents'],newsitems[3]['date']
                                                    ,newsitems[4]['gid'],newsitems[4]['title'],newsitems[4]['url'],newsitems[4]['author'],newsitems[4]['contents'],newsitems[4]['date']
                                                    ,newsitems[5]['gid'],newsitems[5]['title'],newsitems[5]['url'],newsitems[5]['author'],newsitems[5]['contents'],newsitems[5]['date']
                                                    ,newsitems[6]['gid'],newsitems[6]['title'],newsitems[6]['url'],newsitems[6]['author'],newsitems[6]['contents'],newsitems[6]['date']
                                                    ,newsitems[7]['gid'],newsitems[7]['title'],newsitems[7]['url'],newsitems[7]['author'],newsitems[7]['contents'],newsitems[7]['date']
                                                    ,newsitems[8]['gid'],newsitems[8]['title'],newsitems[8]['url'],newsitems[8]['author'],newsitems[8]['contents'],newsitems[8]['date']
                                                    ,newsitems[9]['gid'],newsitems[9]['title'],newsitems[9]['url'],newsitems[9]['author'],newsitems[9]['contents'],newsitems[9]['date']
                                                    ,newsitems[10]['gid'],newsitems[10]['title'],newsitems[10]['url'],newsitems[10]['author'],newsitems[10]['contents'],newsitems[10]['date']
                                                    ,newsitems[11]['gid'],newsitems[11]['title'],newsitems[11]['url'],newsitems[11]['author'],newsitems[11]['contents'],newsitems[11]['date']
                                                    ,newsitems[12]['gid'],newsitems[12]['title'],newsitems[12]['url'],newsitems[12]['author'],newsitems[12]['contents'],newsitems[12]['date']
                                                    ,newsitems[13]['gid'],newsitems[13]['title'],newsitems[13]['url'],newsitems[13]['author'],newsitems[13]['contents'],newsitems[13]['date']
                                                    ,newsitems[14]['gid'],newsitems[14]['title'],newsitems[14]['url'],newsitems[14]['author'],newsitems[14]['contents'],newsitems[14]['date']
                                                    ,newsitems[15]['gid'],newsitems[15]['title'],newsitems[15]['url'],newsitems[15]['author'],newsitems[15]['contents'],newsitems[15]['date']
                                                    ,newsitems[16]['gid'],newsitems[16]['title'],newsitems[16]['url'],newsitems[16]['author'],newsitems[16]['contents'],newsitems[16]['date']
                                                    ,newsitems[17]['gid'],newsitems[17]['title'],newsitems[17]['url'],newsitems[17]['author'],newsitems[17]['contents'],newsitems[17]['date']
                                                    ,newsitems[18]['gid'],newsitems[18]['title'],newsitems[18]['url'],newsitems[18]['author'],newsitems[18]['contents'],newsitems[18]['date']
                                                    ,newsitems[19]['gid'],newsitems[19]['title'],newsitems[19]['url'],newsitems[19]['author'],newsitems[19]['contents'],newsitems[19]['date']
                                                                                                        ,appid, gameName, gameVersion, player_count,
                                                    achievements[0]['name'],achievements[0]['percent']
                                                    ,achievements[1]['name'],achievements[1]['percent']
                                                    ,achievements[2]['name'],achievements[2]['percent']
                                                    ,achievements[3]['name'],achievements[3]['percent']
                                                    ,achievements[4]['name'],achievements[4]['percent']
                                                    ,achievements[5]['name'],achievements[5]['percent']
                                                    ,achievements[6]['name'],achievements[6]['percent']
                                                    ,achievements[7]['name'],achievements[7]['percent']
                                                    ,achievements[8]['name'],achievements[8]['percent']
                                                    ,achievements[9]['name'],achievements[9]['percent']
                                                    ,newsitems[0]['gid'],newsitems[0]['title'],newsitems[0]['url'],newsitems[0]['author'],newsitems[0]['contents'],newsitems[0]['date']
                                                    ,newsitems[1]['gid'],newsitems[1]['title'],newsitems[1]['url'],newsitems[1]['author'],newsitems[1]['contents'],newsitems[1]['date']
                                                    ,newsitems[2]['gid'],newsitems[2]['title'],newsitems[2]['url'],newsitems[2]['author'],newsitems[2]['contents'],newsitems[2]['date']
                                                    ,newsitems[3]['gid'],newsitems[3]['title'],newsitems[3]['url'],newsitems[3]['author'],newsitems[3]['contents'],newsitems[3]['date']
                                                    ,newsitems[4]['gid'],newsitems[4]['title'],newsitems[4]['url'],newsitems[4]['author'],newsitems[4]['contents'],newsitems[4]['date']
                                                    ,newsitems[5]['gid'],newsitems[5]['title'],newsitems[5]['url'],newsitems[5]['author'],newsitems[5]['contents'],newsitems[5]['date']
                                                    ,newsitems[6]['gid'],newsitems[6]['title'],newsitems[6]['url'],newsitems[6]['author'],newsitems[6]['contents'],newsitems[6]['date']
                                                    ,newsitems[7]['gid'],newsitems[7]['title'],newsitems[7]['url'],newsitems[7]['author'],newsitems[7]['contents'],newsitems[7]['date']
                                                    ,newsitems[8]['gid'],newsitems[8]['title'],newsitems[8]['url'],newsitems[8]['author'],newsitems[8]['contents'],newsitems[8]['date']
                                                    ,newsitems[9]['gid'],newsitems[9]['title'],newsitems[9]['url'],newsitems[9]['author'],newsitems[9]['contents'],newsitems[9]['date']
                                                    ,newsitems[10]['gid'],newsitems[10]['title'],newsitems[10]['url'],newsitems[10]['author'],newsitems[10]['contents'],newsitems[10]['date']
                                                    ,newsitems[11]['gid'],newsitems[11]['title'],newsitems[11]['url'],newsitems[11]['author'],newsitems[11]['contents'],newsitems[11]['date']
                                                    ,newsitems[12]['gid'],newsitems[12]['title'],newsitems[12]['url'],newsitems[12]['author'],newsitems[12]['contents'],newsitems[12]['date']
                                                    ,newsitems[13]['gid'],newsitems[13]['title'],newsitems[13]['url'],newsitems[13]['author'],newsitems[13]['contents'],newsitems[13]['date']
                                                    ,newsitems[14]['gid'],newsitems[14]['title'],newsitems[14]['url'],newsitems[14]['author'],newsitems[14]['contents'],newsitems[14]['date']
                                                    ,newsitems[15]['gid'],newsitems[15]['title'],newsitems[15]['url'],newsitems[15]['author'],newsitems[15]['contents'],newsitems[15]['date']
                                                    ,newsitems[16]['gid'],newsitems[16]['title'],newsitems[16]['url'],newsitems[16]['author'],newsitems[16]['contents'],newsitems[16]['date']
                                                    ,newsitems[17]['gid'],newsitems[17]['title'],newsitems[17]['url'],newsitems[17]['author'],newsitems[17]['contents'],newsitems[17]['date']
                                                    ,newsitems[18]['gid'],newsitems[18]['title'],newsitems[18]['url'],newsitems[18]['author'],newsitems[18]['contents'],newsitems[18]['date']
                                                    ,newsitems[19]['gid'],newsitems[19]['title'],newsitems[19]['url'],newsitems[19]['author'],newsitems[19]['contents'],newsitems[19]['date']
                                                                                                        ,appid, gameName, gameVersion, player_count,
                                                    achievements[0]['name'],achievements[0]['percent']
                                                    ,achievements[1]['name'],achievements[1]['percent']
                                                    ,achievements[2]['name'],achievements[2]['percent']
                                                    ,achievements[3]['name'],achievements[3]['percent']
                                                    ,achievements[4]['name'],achievements[4]['percent']
                                                    ,achievements[5]['name'],achievements[5]['percent']
                                                    ,achievements[6]['name'],achievements[6]['percent']
                                                    ,achievements[7]['name'],achievements[7]['percent']
                                                    ,achievements[8]['name'],achievements[8]['percent']
                                                    ,achievements[9]['name'],achievements[9]['percent']
                                                    ,newsitems[0]['gid'],newsitems[0]['title'],newsitems[0]['url'],newsitems[0]['author'],newsitems[0]['contents'],newsitems[0]['date']
                                                    ,newsitems[1]['gid'],newsitems[1]['title'],newsitems[1]['url'],newsitems[1]['author'],newsitems[1]['contents'],newsitems[1]['date']
                                                    ,newsitems[2]['gid'],newsitems[2]['title'],newsitems[2]['url'],newsitems[2]['author'],newsitems[2]['contents'],newsitems[2]['date']
                                                    ,newsitems[3]['gid'],newsitems[3]['title'],newsitems[3]['url'],newsitems[3]['author'],newsitems[3]['contents'],newsitems[3]['date']
                                                    ,newsitems[4]['gid'],newsitems[4]['title'],newsitems[4]['url'],newsitems[4]['author'],newsitems[4]['contents'],newsitems[4]['date']
                                                    ,newsitems[5]['gid'],newsitems[5]['title'],newsitems[5]['url'],newsitems[5]['author'],newsitems[5]['contents'],newsitems[5]['date']
                                                    ,newsitems[6]['gid'],newsitems[6]['title'],newsitems[6]['url'],newsitems[6]['author'],newsitems[6]['contents'],newsitems[6]['date']
                                                    ,newsitems[7]['gid'],newsitems[7]['title'],newsitems[7]['url'],newsitems[7]['author'],newsitems[7]['contents'],newsitems[7]['date']
                                                    ,newsitems[8]['gid'],newsitems[8]['title'],newsitems[8]['url'],newsitems[8]['author'],newsitems[8]['contents'],newsitems[8]['date']
                                                    ,newsitems[9]['gid'],newsitems[9]['title'],newsitems[9]['url'],newsitems[9]['author'],newsitems[9]['contents'],newsitems[9]['date']
                                                    ,newsitems[10]['gid'],newsitems[10]['title'],newsitems[10]['url'],newsitems[10]['author'],newsitems[10]['contents'],newsitems[10]['date']
                                                    ,newsitems[11]['gid'],newsitems[11]['title'],newsitems[11]['url'],newsitems[11]['author'],newsitems[11]['contents'],newsitems[11]['date']
                                                    ,newsitems[12]['gid'],newsitems[12]['title'],newsitems[12]['url'],newsitems[12]['author'],newsitems[12]['contents'],newsitems[12]['date']
                                                    ,newsitems[13]['gid'],newsitems[13]['title'],newsitems[13]['url'],newsitems[13]['author'],newsitems[13]['contents'],newsitems[13]['date']
                                                    ,newsitems[14]['gid'],newsitems[14]['title'],newsitems[14]['url'],newsitems[14]['author'],newsitems[14]['contents'],newsitems[14]['date']
                                                    ,newsitems[15]['gid'],newsitems[15]['title'],newsitems[15]['url'],newsitems[15]['author'],newsitems[15]['contents'],newsitems[15]['date']
                                                    ,newsitems[16]['gid'],newsitems[16]['title'],newsitems[16]['url'],newsitems[16]['author'],newsitems[16]['contents'],newsitems[16]['date']
                                                    ,newsitems[17]['gid'],newsitems[17]['title'],newsitems[17]['url'],newsitems[17]['author'],newsitems[17]['contents'],newsitems[17]['date']
                                                    ,newsitems[18]['gid'],newsitems[18]['title'],newsitems[18]['url'],newsitems[18]['author'],newsitems[18]['contents'],newsitems[18]['date']
                                                    ,newsitems[19]['gid'],newsitems[19]['title'],newsitems[19]['url'],newsitems[19]['author'],newsitems[19]['contents'],newsitems[19]['date']
                                                                                                                                                            ,appid, gameName, gameVersion, player_count,
                                                    achievements[0]['name'],achievements[0]['percent']
                                                    ,achievements[1]['name'],achievements[1]['percent']
                                                    ,achievements[2]['name'],achievements[2]['percent']
                                                    ,achievements[3]['name'],achievements[3]['percent']
                                                    ,achievements[4]['name'],achievements[4]['percent']
                                                    ,achievements[5]['name'],achievements[5]['percent']
                                                    ,achievements[6]['name'],achievements[6]['percent']
                                                    ,achievements[7]['name'],achievements[7]['percent']
                                                    ,achievements[8]['name'],achievements[8]['percent']
                                                    ,achievements[9]['name'],achievements[9]['percent']
                                                    ,newsitems[0]['gid'],newsitems[0]['title'],newsitems[0]['url'],newsitems[0]['author'],newsitems[0]['contents'],newsitems[0]['date']
                                                    ,newsitems[1]['gid'],newsitems[1]['title'],newsitems[1]['url'],newsitems[1]['author'],newsitems[1]['contents'],newsitems[1]['date']
                                                    ,newsitems[2]['gid'],newsitems[2]['title'],newsitems[2]['url'],newsitems[2]['author'],newsitems[2]['contents'],newsitems[2]['date']
                                                    ,newsitems[3]['gid'],newsitems[3]['title'],newsitems[3]['url'],newsitems[3]['author'],newsitems[3]['contents'],newsitems[3]['date']
                                                    ,newsitems[4]['gid'],newsitems[4]['title'],newsitems[4]['url'],newsitems[4]['author'],newsitems[4]['contents'],newsitems[4]['date']
                                                    ,newsitems[5]['gid'],newsitems[5]['title'],newsitems[5]['url'],newsitems[5]['author'],newsitems[5]['contents'],newsitems[5]['date']
                                                    ,newsitems[6]['gid'],newsitems[6]['title'],newsitems[6]['url'],newsitems[6]['author'],newsitems[6]['contents'],newsitems[6]['date']
                                                    ,newsitems[7]['gid'],newsitems[7]['title'],newsitems[7]['url'],newsitems[7]['author'],newsitems[7]['contents'],newsitems[7]['date']
                                                    ,newsitems[8]['gid'],newsitems[8]['title'],newsitems[8]['url'],newsitems[8]['author'],newsitems[8]['contents'],newsitems[8]['date']
                                                    ,newsitems[9]['gid'],newsitems[9]['title'],newsitems[9]['url'],newsitems[9]['author'],newsitems[9]['contents'],newsitems[9]['date']
                                                    ,newsitems[10]['gid'],newsitems[10]['title'],newsitems[10]['url'],newsitems[10]['author'],newsitems[10]['contents'],newsitems[10]['date']
                                                    ,newsitems[11]['gid'],newsitems[11]['title'],newsitems[11]['url'],newsitems[11]['author'],newsitems[11]['contents'],newsitems[11]['date']
                                                    ,newsitems[12]['gid'],newsitems[12]['title'],newsitems[12]['url'],newsitems[12]['author'],newsitems[12]['contents'],newsitems[12]['date']
                                                    ,newsitems[13]['gid'],newsitems[13]['title'],newsitems[13]['url'],newsitems[13]['author'],newsitems[13]['contents'],newsitems[13]['date']
                                                    ,newsitems[14]['gid'],newsitems[14]['title'],newsitems[14]['url'],newsitems[14]['author'],newsitems[14]['contents'],newsitems[14]['date']
                                                    ,newsitems[15]['gid'],newsitems[15]['title'],newsitems[15]['url'],newsitems[15]['author'],newsitems[15]['contents'],newsitems[15]['date']
                                                    ,newsitems[16]['gid'],newsitems[16]['title'],newsitems[16]['url'],newsitems[16]['author'],newsitems[16]['contents'],newsitems[16]['date']
                                                    ,newsitems[17]['gid'],newsitems[17]['title'],newsitems[17]['url'],newsitems[17]['author'],newsitems[17]['contents'],newsitems[17]['date']
                                                    ,newsitems[18]['gid'],newsitems[18]['title'],newsitems[18]['url'],newsitems[18]['author'],newsitems[18]['contents'],newsitems[18]['date']
                                                    ,newsitems[19]['gid'],newsitems[19]['title'],newsitems[19]['url'],newsitems[19]['author'],newsitems[19]['contents'],newsitems[19]['date']
                                                    
                                                    ])
                                fw.flush()
                                time.sleep(1)
                                
                fr.close()
                fw.close()



thread.start_new_thread(SingleThread, ('all_steam_appid01.csv','test01.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid02.csv','test02.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid03.csv','test03.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid04.csv','test04.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid05.csv','test05.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid06.csv','test06.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid07.csv','test07.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid08.csv','test08.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid09.csv','test09.csv'))
thread.start_new_thread(SingleThread, ('all_steam_appid10.csv','test10.csv'))

