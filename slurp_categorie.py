import bs4 as Beautiful
from urllib.request import urlopen
from json import dumps
from os import listdir
from sys import exit


WIKI_LINK = "https://fr.wikipedia.org"
START_PAGE = "https://fr.wikipedia.org/w/index.php?title=Sp%C3%A9cial:Cat%C3%A9gories&limit=5000"
FILE = open('categories.json', 'a+')

def get_next_link(bs4_object):
    link = bs4_object.find('a', class_="mw-nextlink")
    if link:
        return link.get('href')
    else:
        False

def get_and_write_categories(bs4_object, id_counter):
    bs4_object = bs4_object.body.find('ul')
    for li_tag in bs4_object.find_all('a'):
        categorie_id = 'cat' + str(id_counter)
        categories[categorie_id] = {}
        categories[categorie_id]['name'] = li_tag.get_text()
        categories[categorie_id]['url'] = li_tag.get('href')
        id_counter += 1
    return id_counter


id_counter = 0
categories = {}
page = Beautiful.BeautifulSoup(urlopen(START_PAGE), "lxml")
while True:
    id_counter = get_and_write_categories(page, id_counter)
    next_link = get_next_link(page)
    print(id_counter)
    if not next_link:
        print(id_counter, "catégories trouvés")
        break
    else:
        page = Beautiful.BeautifulSoup(urlopen(START_PAGE + next_link), "lxml")
print("Ecriture dans le fichier categories.json au format json")
FILE.write(dumps(categories, indent=4))
print('OK')