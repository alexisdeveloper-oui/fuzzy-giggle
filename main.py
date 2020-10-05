import simplejson as json
import time

with open("inserer path ici", "r") as read_file:
    data = json.load(read_file)

data['messages'].reverse()

espace = '\t\t'

for msg in data['messages']:
    if 'content' in msg:

        oui = str(msg['timestamp_ms'])
        oui = oui[:-2]
        oui = int(oui)
        timestamp = time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(oui))

        if len(msg['sender_name']) > 18:
            espace = '\t\t\t'
        else:
            espace = '\t\t\t\t'

        out = msg['sender_name'] + espace + timestamp + '\t\t' + msg['content']
        out = out.encode('latin1').decode('utf8')
        print(out)
