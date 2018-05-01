from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen("https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Liste_des_portails")
url = url.read()
soup = BeautifulSoup(url, 'lxml')

soup = soup.find('ol').find_all('li')

acc = []

for element in soup:
    acc += [element.string]

print(acc)
