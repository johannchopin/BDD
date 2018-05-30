import json
from urllib.request import urlopen
from urllib.request import quote
import time

with open('bots.json') as json_data:
    data_dict = json.load(json_data)
print('data_dict is created')

def insert_bot_data():
	for element in data_dict:		
		URL = 'http://on.nexioh.eu/isfates_jchopin/bdd/insert_bot_table.php?'
		url = ''
		rela_dict = {
		'id_bot' : element,
		'nom' : quote(data_dict[element]['bot_name']),
		'nb_modification' : data_dict[element]['nb_modif'],
		'statut' : quote(data_dict[element]['is_active'])
		}


		for data_name in rela_dict:
			try:
				int(rela_dict[data_name])
				url += data_name + '=' + str(rela_dict[data_name])
			except:
				url += data_name + '=' + rela_dict[data_name]
			url += '&'

		if data_dict[element]['date_creation'] != None:
			url += 'date_creation' + '=' + data_dict[element]['date_creation']
		if url[-1] == '&':
			url = url[:-1]

		print(URL + url)
		urlopen(URL + url)
		time.sleep(0.005)


insert_bot_data()