'''

import paho.mqtt.subscribe as subscribe

import paho.mqtt.publish as publish
import paho.mqtt.client

topics = 'channels/408316/feeds.json'
#https://api.thingspeak.com/channels/408316/feeds.json?api_key=D45H8ZGPPL9137L6&results=2

sub = subscribe.simple(topics, hostname='mqtt.thingspeak.com', retained=False, msg_count=2)
for a in sub:
    print(a.topic)
    print(a.payload)

'''


import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.thingspeak.com",1883,60)

channelId = "408316"         # Put your channel ID here,i.e.. the number from the URL, https://thingspeak.com/channels/285697
apiKey = "1QL6MDAVNL77XZMY"  # Put the API key here (the Write API Key from the API Keys tab in ThingSpeak)

client.publish("channels/%s/publish/%s" % (channelId,apiKey), "field1=30&field2=40")
client.loop(2)


# https://www.youtube.com/watch?v=yRtc_UKuJuU&feature=youtu.be

