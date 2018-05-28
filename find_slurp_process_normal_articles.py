import bs4 as Beautiful
from urllib.request import urlopen, quote
from json import loads, dumps
from os import listdir, mkdir

STATS_ARTICLE_URL = "https://xtools.wmflabs.org/articleinfo/fr.wikipedia.org/" # Add  url wikipedia
GOAL = 1
FILE = open("stats_normal_articles.json", "w")
PATH_ARTICLES = "articles/normal/"
PATH_JSON = "temp_articles/"
REACH_SOURCES = ['id="Notes_et_références"', 'id="Voir_aussi"', 'id="Liens_externes"']


def make_the_soup_online(page):
    return Beautiful.BeautifulSoup(urlopen(page), 'lxml')

def make_the_soup_local(page):
    return Beautiful.BeautifulSoup(open(page), 'lxml')

def find_type(page):
    try:
        return page.find("a", href="/wiki/Wikip%C3%A9dia:Bons_articles").text
    except:
        try:
            return page.find("a", href="/wiki/Wikip%C3%A9dia:Articles_de_qualit%C3%A9").text
        except:
            return "normal"


def find_categories(page):
    box = page.find("div", id="catlinks").find_all("a")
    categories = [e.get_text() for e in box][1:]
    categories = [e for e in categories if not e.startswith("Portail:") and not e.startswith("Article")]
    return categories

def find_nb_img(contenu):
    return len(contenu.find_all(class_='image'))

def find_author(article_url):
    page_url = "https://fr.wikipedia.org/w/index.php?title=" + quote(article_url.replace(' ', '_')) + "&dir=prev&action=history"
    soup = make_the_soup_online(page_url)
    author = soup.find_all('a', class_ = 'mw-userlink')[-1].text
    return author

def find_nb_parties(page):
    try:
        return len(page.find("div", id="toc").find_all("li"))
    except:
        return 0

def find_nb_link(page, link_in_contents):
    return len(page.find("div", id="content").find_all('a')) - link_in_contents

def find_nb_langues(page):
    page = page.find("div", id="p-lang")
    count = len(page.find_all("li"))
    additionnal = page.find("button", class_="mw-interlanguage-selector mw-ui-button")
    if additionnal != None:
        return count + int(additionnal.get_text())
    else:
        return count

def find_nb_sources(page):
    page = str(page.find("div", id="content"))
    for tag in REACH_SOURCES:
        pos = page.find(tag)
        if tag != -1:
            return page.count("</li>", pos)
    return 0

if not os.path.isdir(PATH_JSON):
    mkdir(PATH_JSON)

stats = {}
files = listdir(PATH_ARTICLES)
target_number = len(files)
for (count, name) in enumerate(files, 1):
    print(target_number, count, name)
    article = make_the_soup_local(PATH_ARTICLES + name)
    id_article = "art" + str(count)
    stats[id_article] = {}
    stats[id_article]["nom"] = name
    stats[id_article]["type"] = find_type(article)
    stats[id_article]["auteur"] = find_author(name) # Open a page
    stats[id_article]["nb_img"] = find_nb_img(article)
    stats[id_article]["nb_parties"] = find_nb_parties(article)
    stats[id_article]["categories"] = find_categories(article)
    stats[id_article]["nb_link"] = find_nb_link(article, stats[id_article]["nb_parties"])
    stats[id_article]["nb_langues"] = find_nb_langues(article)
    stats[id_article]["nb_sources"] = find_nb_sources(article)

    open(PATH_JSON + id_article).write(dumps(stats[id_article], indent=4, ensure_ascii=False))
    # TODO: Append at the end  of the file