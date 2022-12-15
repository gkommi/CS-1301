import requests
counter = 0
for i in range(1, 11):
    url = "https://swapi.dev/api/planets/" + str(i)
    r = requests.get(url)
    data = r.json()
    diameter = int(data['diameter'])
    if diameter >= 10000:
        counter+=1
    else:
        continue
    
#print(counter)

r1 = requests.get("https://ghibliapi.herokuapp.com/films")
print(r1.text[0])

import requests
r = requests.get("https://ghibliapi.herokuapp.com/films")
data = r.json()
info = data[0]
print(type(info))
