import flask
import requests
from bs4 import BeautifulSoup as bs
from flask_restful import Api, Resource, reqparse
import json


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
    parser.add_argument("s")
    parser.add_argument("h")
    parsed = parser.parse_args()
    value_to_go = parsed['s']
    hwid = parsed['h']
    print(hwid)
    print(list)
    if hwid in list:
        to_jsonize = value_to_go.replace('g', '')
        to_jsonize = ''.join(chr(ord(char)-7) for char in to_jsonize)
    else:
        return 'null'
    return flask.jsonify({
"services":
  {
    "twitch":"https://api.twitch.tv/api/channels/",
    "facebook":"https://www.facebook.com/settings",
    "funpay":"https://funpay.ru/account/balance",
    "vk":"https://vk.com/id0",
    "instagram":"https://www.instagram.com/",
    "battlenet":"https://eu.account.blizzard.com/gifts/navbar",
    "steam":"https://store.steampowered.com/account/",
    "youtube":"https://studio.youtube.com/"
  }
})
if __name__ == '__main__':
    app.run(threaded=True, port=5000)

