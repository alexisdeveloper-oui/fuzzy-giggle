from termcolor import colored
import simplejson as json
import glob
import re
from os import path

trig = False

words = []
total = 0
wordcounter = []

if path.exists("words.json") & path.exists("wordcounter.json"):  # & path.exists("you.json"):
    with open('words.json') as json_file:
        words = json.load(json_file)
    with open('wordcounter.json') as json_file:
        wordcounter = json.load(json_file)
    for x in range(len(wordcounter)):
        total += wordcounter[x]
else:
    list_of_files = glob.glob('inbox/*/message_*.json')
    for name in list_of_files:
        print(name)

        with open(name, "r") as read_file:
            data = json.load(read_file)
        if len(data['participants']) <= 2:
            for msg in data['messages']:
                if 'content' in msg:
                    content = msg['content'].encode('latin1').decode('utf8')
                    phrase = content.split()
                    print(phrase)
                    trig = False
                for word in phrase:
                    for x in range(len(words)):
                        if words[x] == word:
                            wordcounter[x] += 1
                            trig = True
                            break
                    if not trig:
                        wordcounter.append(1)
                        words.append(word)
                    print(word)

    # ajouter truc pour pas que accents fuckent
    with open('words.json', 'w') as outfile:
        json.dump(words, open('words.json', 'w'), sort_keys=True, indent=4, separators=(',', ': '))

    with open('wordcounter.json', 'w') as outfile:
        json.dump(wordcounter, open('wordcounter.json', 'w'), sort_keys=True, indent=4, separators=(',', ': '))

wordcounter, words = (list(t) for t in zip(*sorted(zip(wordcounter, words))))

out = ''

for x in range(len(wordcounter)):
    if wordcounter[x] <= 10:
        print('')
    else:
        out += (colored(words[x], 'blue') + " à été envoyé " + colored(str(wordcounter[x]), 'yellow') + " fois \n")

print(out)
# fonction recherche
'''
for line in out.splitlines():
    if re.search('Nom a chercher', line):
        print(line)
'''
# print('\nLe mot le plus utilisé est : ' + colored(words[x], 'red'))

print("\n" + colored("Total de " + str(total) + " messages", 'green', 'on_red'))
