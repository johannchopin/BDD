import os
from bs4 import BeautifulSoup

all_page_file = os.listdir('all_page/')

print(len(all_page_file))


"""
letter_counter = 0
for element in all_page_file:
    mon_fichier = open("all_page/" + element, "r")
    contenu = BeautifulSoup(mon_fichier.read(), 'lxml')

    letter_counter += len(contenu.text)
    print(letter_counter)

print(letter_counter / len(all_page_file))
result -> 68 304
"""

"""
img_counter = 0

for element in all_page_file:
    mon_fichier = open("all_page/" + element, "r")
    contenu = BeautifulSoup(mon_fichier.read(), 'lxml')

    img_counter += len(contenu.find_all('img'))

    print(img_counter)

print(img_counter / len(all_page_file))
result -> 39
"""

"""
href_counter = 0

for element in all_page_file:
    mon_fichier = open("all_page/" + element, "r")
    contenu = BeautifulSoup(mon_fichier.read(), 'lxml')

    href_counter += len(contenu.find_all('a'))

    print(href_counter)

print(href_counter / len(all_page_file))
result -> 1203
"""

"""
img_visible_counter = 0

for element in all_page_file:
    mon_fichier = open("all_page/" + element, "r")
    contenu = BeautifulSoup(mon_fichier.read(), 'lxml')

    img_visible_counter += len(contenu.find_all(class_="thumbimage"))

    print(img_visible_counter)

print(img_visible_counter / len(all_page_file))
result -> 12
"""

"""
references_counter = 0
counter = 0

for element in all_page_file:
    mon_fichier = open("all_page/" + element, "r")
    contenu = BeautifulSoup(mon_fichier.read(), 'lxml')

    references_counter += len(contenu.find_all('span', class_="noprint renvois_vers_le_texte"))
    counter += 1

    print(counter)

print(references_counter / len(all_page_file))
result -> 63
"""

"""
sommaire_counter = 0
counter = 0

for element in all_page_file:
    mon_fichier = open("all_page/" + element, "r")
    contenu = BeautifulSoup(mon_fichier.read(), 'lxml')

    sommaire_len = contenu.find('div', class_="toc")

    if sommaire_len != None:
        sommaire_len = len(sommaire_len.find_all('a'))

    else:	
        sommaire_len = 0

    sommaire_counter += sommaire_len
    counter += 1

    print(counter)

print(sommaire_counter / len(all_page_file))
result -> 32
"""


