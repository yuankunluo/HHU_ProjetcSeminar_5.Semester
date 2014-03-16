# -*- coding: utf-8 -*-

import pickle

with open("data/Wolfgang G. Stock_raw.db") as f: 
	data = pickle.load(f)

titles = [] 
for d in data: 
	title = d['title'] 
	titles.append(title)
for i in range(len(titles)): 
	print(titles[i])
