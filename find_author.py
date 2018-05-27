from bs4 import BeautifulSoup
from urllib.request import urlopen

ARTICLE_EXAMPLE_URL_NAME = "https://fr.wikipedia.org/wiki/(30704)_Ph%C3%A9g%C3%A9e"
global len_url_to_del
len_url_to_del = len("https://fr.wikipedia.org/wiki/")

def make_the_soup(page):
	url = urlopen(page)
	url = url.read()
	soup = BeautifulSoup(url, 'lxml')
	return soup


def find_author(articles_url):
	global len_url_to_del
	articles_name_url_format = articles_url[len_url_to_del:]
	page_url = "https://fr.wikipedia.org/w/index.php?title=" + (articles_name_url_format) + "&dir=prev&limit=20&action=history"
	soup = make_the_soup(page_url)
	author = soup.find_all('a', class_ = 'mw-userlink')[-1].text
	print(author)
	return author

find_author(ARTICLE_EXAMPLE_URL_NAME)
