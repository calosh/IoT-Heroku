import urllib2
import json
import time


READ_API_KEY='   '
CHANNEL_ID= '    '


while True:
    TS = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,READ_API_KEY))

    response = TS.read()
    data=json.loads(response)


    a = data['created_at']
    b = data['field1']
    c = data['field2']
    d = data['field3']
    print a + "    " + b + "    " + c + "    " + d
    time.sleep(5)

    TS.close()


# https://stackoverflow.com/questions/41089487/python-get-data-through-thingspeak