import os
from bs4 import BeautifulSoup


mon_fichier = open("all_page_article_de_qualite/Affaire_Elizabeth_Canning.txt", "r")
contenu_test = BeautifulSoup(mon_fichier.read(), 'lxml') 

"""
def slurp_data():
    all_page_file = os.listdir('all_page_article_de_qualite/')
    for article_name in all_page_file:
		mon_fichier = open("all_page_article_de_qualite/" + article_name, "r")
		contenu = BeautifulSoup(mon_fichier.read(), 'lxml')
	return 2
"""

def word_counter(contenu):
	result_data = len((contenu.text).split(" "))
	print(result_data)
	return result_data

#word_counter(contenu_test)


#PROBLEM ADD IMAGE TITLE
def visible_img_counter(contenu):
    result_data = len(contenu.find_all(class_='image'))
    print(result_data)
    return result_data

#visible_img_counter(contenu_test)



def href_counter(contenu):
    result_data = len(contenu.find_all('a'))
    print(result_data)
    return result_data

#href_counter(contenu_test)

#DONT WORK
def references_counter(contenu):
	for element in contenu.find_all('ol', class_='references'):
		print(element.parent.previous_sibling)
	return result_data

#references_counter(contenu_test)


def parties_counter(contenu):
    result_data = contenu.find_all('div', class_="toc")
    for element in result_data:
	    if element.find('h2').get_text() == 'Sommaire':
	    	for number in element.find_all('span', class_='tocnumber'):
	    		number = number.get_text()
	    		try:
	    			print(int(number))
	    		except:
	    			print("number")
    return result_data

parties_counter(contenu_test)