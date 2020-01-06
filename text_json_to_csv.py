# -*- coding: utf-8 -*-
import json
import pandas as pd
import re
from pprint import pprint

special_chars =['\n','?','.','+','~','-','_','!','@','#','#','$','%','^','&','*','(',')','{','}','[',']','/','=','|',',']


def cleanText(x,notwanted):
 
    #텍스트에 포함되어 있는 특수 문자 제거 (Remove special characters)
    for item in notwanted:
        x = x.replace(item,' ')
    return x

with open('file_name.json','r',encoding = 'UTF-8') as f:
    json_data = json.load(f)

text = []
num = []

for i,e in enumerate(json_data['GraphImages']):
    #print(i,e)
    if e['edge_media_to_caption']['edges'] == []: continue
    text.append((e['edge_media_to_caption']['edges'][0]['node']['text']))

text = list(set(text))
num.append(len(text))

for e in range(len(text)):
    text[e] = cleanText(text[e],special_chars)
    text[e] = re.sub('[^가-힣]', ' ', text[e])
   

df = pd.DataFrame(text, columns=['보령'])
######################################################################################################################

df.to_csv('file_name.csv',encoding='utf-8-sig')

print(num)