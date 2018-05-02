from sys import exit, argv
from os import mkdir, listdir
from datetime import datetime 
from urllib.request import unquote
try:
    import wikipedia
except ImportError:
    print('Please install the wikipedia\'s API')

# ===========
# initization 
# ===========

wikipedia.set_lang('fr')
wikipedia.set_rate_limiting(True) # Avoid spamming to the server

ADQ = set(open('all_titles_article_de_qualite.txt').read().lower().split('\n'))
BA = set(open('all_titles_bon_article.txt').read().lower().split('\n'))
downloaded = set([e.lower() for e in listdir('articles/normal')]).union(ADQ).union(BA)

# If a parameter are given to the script,
# bound equal to the parameter, else 100 000
bound = int(argv[1]) if len(argv) > 1 else 100000

# ====
# core 
# ====

while len(downloaded) <= bound:

    try:
        # Get the title of the first reference in wikipedia, avoid some DisambiguationError
        title = wikipedia.search(wikipedia.random(), results=1)[0]
        article = wikipedia.WikipediaPage(title).html()
    except wikipedia.exceptions.DisambiguationError:
        print('DisambiguationError')
    else:
        title = title.replace('\\', ' ')
        if title.lower() not in downloaded:
            with open("articles/normal/" + title, 'x') as f:
                f.write(article)
            downloaded.add(title.lower())
            print(f"{title}")