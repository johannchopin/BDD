import re
import bs4 as Beautiful
from json import loads, dumps
from urllib.request import urlopen
from os.path import isfile

START_PAGE = "https://fr.wikipedia.org"
CATEGORIES = loads(open('categories.json').read())

def trial_1(page):
    try:
        number = page.body.find("div", id="mw-pages").find('p').get_text().split(' ')[4]
        portails = page.find('table', class_="bandeau-categorie")
        portails = portails.find_all("a", href=re.compile(r"/wiki/Portail:[\w]+$"))
        portails = [e.get("title")[8:] for e in portails]
        return portails
    except:
        return False

def trial_2(page):
    try:
        portails = page.body.find("div", class_="cadre_portail").find("td", width="100%").find("a", title=re.compile("Catégorie:*"))
        portails = portails.get("href")[10:]
        return portails
    except:
        return False

def case_special(d, id_category, value):
    del d[id_category]["url"]
    categorie_update[id_category]["portail_linked"] = value

categorie_update = CATEGORIES
step = 100/len(CATEGORIES)
acc = step
for id_category in CATEGORIES:
    if isfile("temp/" + id_category):
        print(f"{acc:{1}.{5}}%")
        acc += step
        continue
    if CATEGORIES[id_category]["url"].startswith("/w/index.php"):
        case_special(categorie_update, id_category, None)
        open("temp/" + id_category, 'w').write(dumps(categorie_update[id_category]))
        print(f"{acc:{1}.{5}}%")
        acc += step
        continue
    
    page = Beautiful.BeautifulSoup(urlopen(START_PAGE + CATEGORIES[id_category]["url"]), "lxml")
    portails = trial_1(page)
    if portails == False:
        portails = trial_2(page)
        
        if portails == False:
            case_special(categorie_update, id_category, "Aucun portail direct")
            open("temp/" + id_category, 'w').write(dumps(categorie_update[id_category]))
            print(f"{acc:{1}.{5}}%")
            acc += step
            continue

    #Update categories if all normal
    del categorie_update[id_category]["url"]
    categorie_update[id_category]["portail_linked"] = portails

    open("temp/" + id_category, 'w').write(dumps(categorie_update[id_category]))
    # Printing
    print(f"{acc:{1}.{5}}%")
    acc += step

# Build the 