#Membuat Dictionary
thisdict = {
  "brand": "Channel",
  "model": "Hera",
  "year": 2025,
  "year": 2026
}
print(thisdict)
print(len(thisdict))        #Panjang item

thisdict = {
  "brand": "Gucci",
  "electric": True,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
print(type(thisdict))       #Tipe data

#Konstruktor dict
thisdict = dict(name = "Hera", age = 19, country = "Dubai")
print(thisdict) 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()

#Mengganti dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

#Menambah dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

#Menghapus
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Mengulangi
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#Mengcopy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Nested
child1 = {
  "name" : "Hera",
  "year" : 2006
}
child2 = {
  "name" : "Yazid",
  "year" : 2010
}
child3 = {
  "name" : "Fairuz",
  "year" : 2014
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(myfamily["child2"]["name"])
