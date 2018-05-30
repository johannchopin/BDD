import json
from urllib.request import urlopen
from urllib.request import quote
import time


with open('rela_bot_contr.json') as json_data:
    data_dict = json.load(json_data)
print('data_dict is created')

def insert_bot_for_key():	
	for element in data_dict:		
		URL = 'http://on.nexioh.eu/isfates_jchopin/bdd/insert_bot_table.php?'
		url = ''
		rela_dict = {
		'id_contributeur' : element,
		'id_bot' : data_dict[element]['bots']
		}

		for data_name in rela_dict:
			url += data_name + '=' + rela_dict[data_name] + '&'
		if url[-1] == '&':
			url = url[:-1]

		print(URL + url)
		urlopen(URL + url)
		time.sleep(0.005)

insert_bot_for_key()