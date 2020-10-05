from termcolor import colored
import simplejson as json
import glob
import re
from os import path

trig = False

auteurs = []
total = 0
counter = [0, 0, 0]

if path.exists("auteurs.json") & path.exists("counter.json"):  # & path.exists("you.json"):
    with open('auteurs.json') as json_file:
        auteurs = json.load(json_file)
    with open('counter.json') as json_file:
        counter = json.load(json_file)
    for x in range(len(counter)):
        total += counter[x]
else:
    list_of_files = glob.glob('inbox/*/message_*.json')
    for name in list_of_files:
        print(name)

        with open(name, "r") as read_file:
            data = json.load(read_file)
        if len(data['participants']) <= 2:
            for msg in data['messages']:
                sender = msg['sender_name'].encode('latin1').decode('utf8')
                trig = False
                for x in range(len(auteurs)):
                    if auteurs[x] == sender:
                        counter[x] += 1
                        trig = True
                        break
                if not trig:
                    auteurs.append(sender)
                    counter.append(1)
                total += 1
    # ajouter truc pour pas que accents fuckent
    with open('auteurs.json', 'w') as outfile:
        json.dump(auteurs, open('auteurs.json', 'w'), sort_keys=True, indent=4, separators=(',', ': '))

    with open('counter.json', 'w') as outfile:
        json.dump(counter, open('counter.json', 'w'), sort_keys=True, indent=4, separators=(',', ': '))

    x = 0

counter, auteurs = (list(t) for t in zip(*sorted(zip(counter, auteurs))))

out = ''

for x in range(len(auteurs)):
    if counter[x] <= 20:
        out += (auteurs[x] + ' est crissement rejet\n')
    else:
        out += (colored(auteurs[x], 'blue') + " à envoyé " + colored(str(counter[x]), 'yellow') + " messages, donc " + str(
            round(((counter[x] / total) * 100), 2)) + "% des messages\n")

print(out)
# fonction recherche
'''
for line in out.splitlines():
    if re.search('Marchand', line):
        print(line)
'''
print('\nVous êtes ' + colored(auteurs[x], 'red'))

print("\n" + colored("Total de " + str(total) + " messages", 'green', 'on_red'))
