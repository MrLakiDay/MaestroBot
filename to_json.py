import json


cenz_list = []

with open("cenz_words.txt", encoding = "utf-8") as r:
	for i in r:
		n = i.lower().split(",")[0]
		if n != "":
			cenz_list.append(n)

with open("cenz.json", "w", encoding = "utf-8") as e:
	json.dump(cenz_list, e)			
