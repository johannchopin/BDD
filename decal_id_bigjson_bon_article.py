from json import loads, dumps

with open('BigJsonArticleBon.json', 'r') as f:
    d = loads(f.read())

d2 = {}
for (count, key) in enumerate(d):
    d2["art" + str(int(key[3:-4]) + 101681)] = d[key]
    print(count)

print("Writing")
with open('BigJsonArticleBon2.json', 'w') as f:
    f.write(dumps(d2, indent=4, ensure_ascii=False))