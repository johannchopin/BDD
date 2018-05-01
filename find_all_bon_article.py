from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
url = urlopen("https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Article_de_qualit%C3%A9")
contenu = BeautifulSoup(url.read(), 'lxml')

all_article_de_qualite = contenu.find('div', class_="CategoryIndex liste-horizontale").find_all(class_="external text")


final_list = []
for element in all_article_de_qualite:
    final_list += [element.string]
"""


"""
all_bon_article_lien_list = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

all_bon_article_lien = []
URL = "https://fr.wikipedia.org/w/index.php?title=Cat" + quote("é") + "gorie:Bon_article&from="

counter = 0

print_list = []
for element in all_bon_article_lien_list:
    url = urlopen(URL + element)
    url = url.read()
    soup = BeautifulSoup(url, 'lxml')


    soup = soup.find(class_="mw-category-group").find_all('a')
    for element in soup:
        print_list += [element.get('href')]
        print(counter)
        counter += 1

print(print_list)
"""


mon_fichier = open("all_bon_article_lien_list.txt", "r")
contenu = mon_fichier.read()

exec(contenu)

counter = 0
for element in all_bon_article_lien_list:
    print(counter)
    if counter > 1422:
        url = urlopen("https://fr.wikipedia.org" + element)
        url = url.read()
        soup = BeautifulSoup(url, 'lxml')

        create_file = open("all_page_bon_article/" + element[6:] + ".txt", 'w')
        create_file.write(str(soup))
        create_file.close()
    counter += 1
