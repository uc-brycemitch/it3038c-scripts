import json
import requests

r = requests.get('http://localhost:3000')

data = r.json()


for w in range(len(data)):
    print("{} is {}.".format(data[w]["name"], data[w]["color"]))

#print(data)