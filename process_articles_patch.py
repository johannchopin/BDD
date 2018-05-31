from json import loads, dumps
from urllib.request import urlopen, quote
import bs4

PATH_NORMAL = "articles_brut/bon_article/"
REACH_SOURCES = ['id="Références', 'id="Notes_et_références"', 'id="Voir_aussi"', 'id="Liens_externes"']

def find_nb_sources(page):
    sources_possible = [page.count("li>" ,page.find(tag)) for tag in REACH_SOURCES]
    return max(0, max(sources_possible))

print("Reading and loading BigJson")
with open('BigJson.json') as f:
    d = loads(f.read())

to_del = []
for (count, key) in enumerate(d, 0):
    type_art = d[key]['type']
    nom = d[key]['nom']
    if type_art != "normal":
        nom = nom.replace(' ', '_')

    try:
        with open(PATH_NORMAL+nom) as f:
            page = bs4.BeautifulSoup(f.read(), "lxml")
            page = str(page.find("div", id="content"))
            d[key]['nb_sources'] = find_nb_sources(page)
            d[key]['nb_mots'] = page.count(' ')
    except:
        to_del.append(key)

    print(count, type_art)
    
print("Suppression des clés")
for key in to_del:
    del d[key]
print("Writing BigJsonArticleBon")
with open('BigJsonArticleBon.json', 'w') as f:
    f.write(dumps(d, indent=4, ensure_ascii=False))