from json import loads, dumps
from os.path import isfile
from os import listdir

PATH_BON = 'articles/bon/'
PATH_DE_QUALITE = 'articles/de_qualite/'
PATH_NORMAL = 'temp_articles/' # articles in HTML are in articles/normal/
BIG_JSON = 'BigJson.json'
PATH = PATH_NORMAL # Change to add a new type of articles

# Initialize with file BIG_JSON (for the gap between new_id with count)
if isfile(BIG_JSON):
    with open(BIG_JSON) as f:
        big_json = loads(f.read())
        count = len(big_json)
else:
    count = 0
    big_json = {}

# Update big_json with each json file
for file in listdir(PATH):
    new_id = 'art' + str(count)
    with open(PATH + file) as f:
        big_json[new_id] = {}
        big_json[new_id].update(loads(f.read()))
    count += 1
    print(count)

# Write updated big_json
with open(BIG_JSON, 'w') as f:
    f.write(dumps(big_json, ensure_ascii=False, indent=4))