from json import loads, dumps
from os import listdir

print("loading BigJson")
with open('BigJson.json') as f:
    d = loads(f.read())

for (count, key) in enumerate(d, 1):
    cat = d[key]["categories"]
    d[key]["categories"] = [e for e in cat if not e.startswith("Projet:") and not e.startswith("Page") and not e.startswith("Wikipédia:")]
    print(count)

print("Writing BigJson")
with open('BigJson.json', 'w') as f:
    f.write(dumps(d, ensure_ascii=False, indent=4))
