
from urllib.request import urlopen
from bs4 import BeautifulSoup


mon_fichier = open("web_site_url.txt", "r")
contenu = mon_fichier.read()

exec(contenu)

counter = 0

for element in href_list:

    counter += 1
    url = urlopen(element)
    url = url.read()
    soup = BeautifulSoup(url, 'lxml')
    
    create_file = open("all_page/" + element[30:] + ".txt", 'w')
    create_file.write(str(soup))
    create_file.close()

    print(counter)

mon_fichier.close()
