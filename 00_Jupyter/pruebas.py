i = 0
list_numbers = list()

while len(list_numbers) < 100:
    list_numbers.append(i)
    i = i+2

print(list_numbers)
print(len(list_numbers))

import pandas as pd
import string

w = string.ascii_uppercase

for i in w:
    print(i)


data={'Islands':["Gran Canaria","Tenerife","La Palma","Lanzarote","La Gomera","El Hierro","Furteventura"],
      'Population':[855521,928604,83458,155812,21678,11147,119732],
      'Area':[1560.1,2034.38,708.32,845.94,369.76,278.71,1659],
      'Province':["LPGC","SCTF","SCTF","LPGC","SCTF","SCTF","LPGC"]}

democan = pd.DataFrame(data)
print(democan)