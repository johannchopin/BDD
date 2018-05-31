from json import loads, dumps
from urllib.request import unquote

print("Lecture BigCategories")
with open("BigCategories.json") as f:
    d = loads(f.read())

for (count, key) in enumerate(d):
    links = d[key]["portail_linked"]
    if type(links) == list and len(links) > 0:
        d[key]["portail_linked"] = [unquote(e) for e in links]
    else:
        d[key]["portail_linked"] = "Aucun portail direct"
    print(count)

print("Writing in file")
with open("BigCategories2.json", "w") as f:
    f.write(dumps(d, indent=4, ensure_ascii=False))