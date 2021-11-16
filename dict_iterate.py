dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


dicts =[]
dicts.append(dict1)
dicts.append(dict2)

for each_val in dicts:
    for key,val in each_val.items():
        print(key,val)
    
print("Hello World")
