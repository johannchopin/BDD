from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen("https://fr.wikipedia.org/wiki/Portail:Accueil")
url = url.read()
soup = BeautifulSoup(url, 'lxml')

soup = soup.find_all('td')

acc = []

for element in soup:
    acc += [element.find('li')]

print(acc)
