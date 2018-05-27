from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import unquote, quote
import json
from json import dumps


with open('contributeurs_data.json') as json_data:
    data_dict = json.load(json_data)
print('data_dict is created')

global counter
global len_data_dict
counter = 0
len_data_dict = str(len(data_dict))


def add_first_contribution(data_dict):
	global counter
	global len_data_dict
	for element in data_dict:
		url_name = quote(data_dict[element]['name'].replace(' ', '_'))
		url = 'https://fr.wikipedia.org/w/index.php?title=Sp%C3%A9cial:Contributions/'+ url_name + '&dir=prev&limit=20'
		date = find_first_contribution(url)		
		data_dict[element]['first_contr'] = date
		print(str(counter) + ' / ' + len_data_dict)
		counter += 1	
	open('contributeurs_data_up.json', 'w').write(dumps(data_dict, indent=4, ensure_ascii=False))
	return "END"


def find_first_contribution(page):
	soup = make_the_soup(page)
	try:
		first_contribution = soup.find_all('a', class_ = 'mw-changeslist-date')[-1].text
		return first_contribution
	except:
		print(page)
		return None


def make_the_soup(page):
	url = urlopen(page)
	soup = BeautifulSoup(url, 'lxml')
	return soup

add_first_contribution(data_dict)