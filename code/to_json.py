from csv import DictReader
from itertools import groupby
from pprint import pprint
import json

def get_buffs(l):
	buff_dict = {}
	for i in l:
		try: # for foods without buff specification
			buff_dict['buff'] = i.split('+')[0].lstrip()
			buff_dict['value'] = i.split('+')[1].lstrip()
		except:
			buff_dict['buff'] = i.lstrip()
			buff_dict['value'] = ''
	return buff_dict


with open('data/cook_list.csv') as csvfile:
	r = DictReader(csvfile, skipinitialspace=True, delimiter=';')
	data = [dict(d) for d in r]

	groups = []
	uniquekeys = []

	for k, g in groupby(data, lambda r: (r['ï»¿recipe_name'], r['buff_effect'], r['utensil'])):
		groups.append({
			"recipe_name": k[0],
			"utensil": k[2],
			"ingredients": [{k:v for k, v in d.items() if k not in ['ï»¿recipe_name','buff_effect', 'utensil']} for d in list(g)],
			"buff_effect": get_buffs(k[1].split(','))
		})
		uniquekeys.append(k)

with open('data/cook_list.json', 'w') as outfile:
	json.dump(groups, outfile)