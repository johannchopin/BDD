from sys import exit, argv
from os import mkdir, listdir
from urllib.request import urlopen
import bs4 as Beautiful

# ===========
# initization 
# ===========

RANDOM_ARTICLE_URL = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
downloaded = set([e.lower() for e in listdir('articles/normal')])

# If a parameter are given to the script,
# bound equal to the parameter, else 100 000
bound = int(argv[1]) if len(argv) > 1 else 100027

# ====
# core 
# ====

while len(downloaded) <= bound:
    article = Beautiful.BeautifulSoup(urlopen(RANDOM_ARTICLE_URL), "lxml")
    title = article.find("h1").get_text()
    title = title.replace('\\', ':')
    try:
        with open("articles/normal/" + title, 'x') as f:
            f.write(str(article))
            downloaded.add(title.lower())
            print(f"{title}")
    except FileExistsError:
        pass
    except FileNotFoundError:
        pass