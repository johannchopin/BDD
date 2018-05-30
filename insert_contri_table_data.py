import json
from urllib.request import urlopen
from urllib.request import quote
import time

with open('contributeurs_data_v2.json') as json_data:
    data_dict = json.load(json_data)
print('data_dict is created')


def insert_contri_data():
	counter = 0
	len_element = len(data_dict)
	for element in data_dict:		
		URL = 'http://on.nexioh.eu/isfates_jchopin/bdd/insert_contri_table.php?'
		url = ''
		rela_dict = {
		'id_contributeur' : element,
		'nom' : quote(data_dict[element]['name'])
		}


		for data_name in rela_dict:
			try:
				int(rela_dict[data_name])
				url += data_name + '=' + str(rela_dict[data_name])
			except:
				url += data_name + '=' + rela_dict[data_name]
			url += '&'

		if data_dict[element]['first_contr'] != None:
			url += 'date_pre_contr' + '=' + quote(data_dict[element]['first_contr'])
		if data_dict[element]['page_url'] != None:
			url += '&page_perso=1'
		else:
			url += '&page_perso=0'

		if url[-1] == '&':
			url = url[:-1]

		print(str(counter) + ' / ' + str(len_element))
		counter += 1
		urlopen(URL + url)
		time.sleep(0.005)

insert_contri_data()