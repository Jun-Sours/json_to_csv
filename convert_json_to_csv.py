import json
import csv
from pprint import pprint


with open('file.json','r',encoding = 'UTF-8') as f:
    json_data = json.load(f)


tags =[]
id = []
dic = {}
for e in json_data['GraphImages']:
    tags.append(e['tags'])
    id.append(e['owner'].get('id'))

for i in range(len(tags)):
    tags[i] = ",".join(tags[i])

for f in range(len(tags)):
    dic[id[f]]=tags[f]


with open('file.csv','w',encoding='utf-8-sig')as f:
   w = csv.DictWriter(f,dic.keys())
   w.writeheader()
   w.writerow(dic)


