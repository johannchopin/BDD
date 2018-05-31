from json import loads, dumps
from os import listdir

PATH = "categories_json/"
FILES = listdir(PATH)

big_json = {}
for (count, file) in enumerate(FILES):
    big_json[file] = {}
    try:
        with open(PATH + file) as f:
            big_json[file].update(loads(f.read()))
    except:
        del big_json[file]
    print(count)

with open("BigCategories.json", 'w') as f:
    f.write(dumps(big_json, indent=4, ensure_ascii=False))