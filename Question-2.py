# Write a program that is able to return the meaning of an English language word provided to it in the terminal. (Use https://dictionaryapi.dev/)

import requests
word = str(input('Enter a word : '))
URL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+word
r = requests.get(url = URL)
data = r.json()
for i in data[0]['meanings'] :
	print(i['partOfSpeech'].capitalize(),' ',i['definitions'][0]['definition'])
