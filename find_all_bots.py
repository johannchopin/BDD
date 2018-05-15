from json import dumps
from urllib.request import urlopen
from urllib.parse import unquote
import bs4 as Beautiful
import re

FILENAME = "bots.json"
# ID_du_BOT : bot-<numéro>
# nom du bot
# date_de_création
# nb_modification
URL = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Bot/Liste"
creator_regex = re.compile('^/wiki/Utilisateur')
data = {}

rows = Beautiful.BeautifulSoup(urlopen(URL).read(), "lxml").find_all('tr')[1:-1]
print("Table Tag téléchargé")

size = len(rows)
for (count, row) in enumerate(rows, 1):
    cols = row.contents[1::2] # Format list
    id_bot = "bot" + str(count)
    data[id_bot] = {}
    
    data[id_bot]['bot_name'] = cols[0].a.get_text()
    
    try: # Some bots have a unknow creator
        data[id_bot]['createur'] = cols[1].a.get_text()
    except:
        data[id_bot]['createur'] = None

    try: # Some bots don't have a date
        data[id_bot]['date_creation'] = cols[2].span.get_text()[:10]
    except:
        data[id_bot]['date_creation'] = None

    data[id_bot]['nb_modif'] = int(cols[4].get_text())
    
    data[id_bot]['is_active'] = cols[-1].a.get_text()
    print(count, '/', size)

print("All bot's informations downloaded")
with open(FILENAME,'w') as f:
    f.write(dumps(data, indent=4))
with open(FILENAME,'r+') as f:
    data = f.read().replace(r'\u00e9', 'é')
    f.write(data)
print("Data written in file %s" % FILENAME)

# Need to replace manually 
# "\u05d8\u05d1\u05e2\u05ea-\u05d6\u05e8\u05dd" -> "טבעת-זרם"
# "\u00e9" -> "é"
# "\u00e1" -> "á"

# SOlution : replace(u"<4 char>", "special_char")