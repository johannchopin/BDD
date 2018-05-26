from urllib.request import urlopen
from bs4 import BeautifulSoup
from json import dumps


URL = "https://fr.wikipedia.org/w/index.php?title=Sp%C3%A9cial:Utilisateurs_actifs&offset=&limit=500"
WIKI_URL = 'https://fr.wikipedia.org'

all_data = {}
global counter
counter = 0

def find_all_contributeurs(url):
	soup = make_the_soup(url)
	process_page(soup)
	try:
		next_link = soup.find('a', class_ = 'mw-nextlink')
		find_all_contributeurs(WIKI_URL + next_link.get('href'))
	except:
		print('write')
		open('contributeurs_data.json', 'w').write(dumps(all_data, indent=4, ensure_ascii=False))
		return "END"

def make_the_soup(page):
	url = urlopen(page)
	url = url.read()
	soup = BeautifulSoup(url, 'lxml')
	return soup

def process_page(soup):
	global counter
	contributeurs = soup.find_all('a', class_ = 'mw-userlink')
	for element in contributeurs:
		contributeur_name = element.get_text()
		contributeurs_page = element.get('href').split('&')[0]
		if '/w/index.php?title=Utilisateur:' in contributeurs_page:
			contributeurs_page = None
		data = (contributeurs_page, contributeur_name)
		all_data['contr' + str(counter)] = {}
		all_data['contr' + str(counter)]['page_url'] = data[0]
		all_data['contr' + str(counter)]['name'] = data[1]
		print(counter)
		counter += 1


find_all_contributeurs(URL)