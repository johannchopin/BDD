
from urllib.request import urlopen
from bs4 import BeautifulSoup


mon_fichier = open("web_site_url.txt", "r")
contenu = mon_fichier.read()

exec(contenu)

openfile =  open('all_page.txt', mode = 'a')
counter = 0
openfile.write('all_page_list = [')

for element in href_list:
    counter += 1
    url = urlopen(element)
    url = url.read()
    soup = BeautifulSoup(url, 'lxml')
    openfile.write('["""' + str(soup) + '"""],')
    print(counter)

openfile.write(']')

openfile.close()

mon_fichier.close()
