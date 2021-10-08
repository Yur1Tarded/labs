import json
f = open('pokemon_full.json')
full = f.read()
print(f'Общее количество символов - {len(full)}')
c = 0
for i in range(len(full)):
    if full[i] not in ')(}{][.,-_=%&#@:/!?+*$~`;^<>\|/ „‚¬"' and full[i]!="'" and full[i]!='\n':
        c+=1
print(f'Символов без знаков препинания и пробелов - {c}')
pokemon = json.loads(full)
maxdescr = ['', '', 0]
for i in pokemon:
    if len(i.get('description'))>maxdescr[2]:
        maxdescr[2] = len(i.get('description'))
        maxdescr[0] = i.get('name')
        maxdescr[1] = i.get('description')
print(f'Самое длинное описание у покемона {maxdescr[0]}, оно имеет длину {maxdescr[2]} симв. и выглядит так:')
print(maxdescr[1])
maxabil = ['', '', 0]
for i in pokemon:
    for j in i.get('abilities'):
        if len(j.split())>maxabil[2]:
            maxabil[2] = len(j.split())
            maxabil[0] = i.get('name')
            maxabil[1] = j
print(f'Самое большое кол-во слов в названии способности покемона {maxabil[0]}, оно имеет длину {maxabil[2]} сл. и выглядит так:')
print(maxabil[1])
