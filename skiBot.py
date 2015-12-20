import time
import json
from slackclient import SlackClient

with open('config.json') as c:
    config = json.loads(c.read())


sc = SlackClient(config['token'])


user = sc.server.channels.find(config['user'])
if sc.rtm_connect():
    while True:
        data = sc.rtm_read()
        for d in data:
            if 'text' in d and 'user' in d and 'channel' in d:
                if d['user'] == user:
                    continue
                
                print d
                
                sc.rtm_send_message(d['channel'], d['text'])
        time.sleep(.1)
else:
    print "Connection Failed, invalid token?"
