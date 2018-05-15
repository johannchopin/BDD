from json import dumps
from urllib.request import urlopen
from urllib.parse import unquote
import bs4 as Beautiful

FILENAME = "bots.json"
URL = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Bot/Liste"
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
# Solution : replace(u"<4 char>", "special_char")