import json
from json import loads, dumps
from os import listdir, mkdir


global PATH_ARTICLES, TYPE
PATH_ARTICLES = 'temp_articles'
PATH_COPY = 'temp_articles_v2'
TYPE = 'bon'

def add_type_cheat():
	global PATH_ARTICLES, TYPE
	for element in listdir(PATH_ARTICLES):
		with open(PATH_ARTICLES + '/' + element) as json_data:
		    data_dict = json.load(json_data)
		print('data_dict is created')
		data_dict['type'] = TYPE
		open(PATH_COPY + '/' + element, 'w').write(dumps(data_dict, indent=4, ensure_ascii=False))

add_type_cheat()



