from urllib.request import unquote

# Same with all_bon_article_lien_list.txt
adq = open('all_article_de_qualite_lien_list.txt').read()
adq = adq.replace('\n', '').replace('[', '').replace(']', '').replace('_', ' ').split(', ')
titles = [unquote(link[7:-1]) for link in adq]
for title in titles:
    print(title)
    # Redirected in file with Bash