#Mengatur set
negara = {"Inggris", "Amerika", "Indonesia"}
print(negara)

negara = {"Amerika", "Korea", "Indonesia", "Korea"}
print(negara)   #Duplikat tidak diizinkan

thisset = {"Amerika", "Malaysia", "Korea", True, 1, 2}
print(thisset)     #True dan 1 dianggap bernilai sama

thisset = {"Amerika", "Malaysia", "Korea", False, 0, 2}
print(thisset)      #False dan 0 dianggap bernilai sama

negara = {"Amerika", "Korea", "Indonesia", "Malaysia"}
print(len(negara))      #Menghitung Panjang Satu Set

set1 = {"Indonesia", "Malaysia", "Singapura"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, True}

print(set1)
print(set2)
print(set3)     #Item dalam himpunan dapat berupa tipe data apa pun

set1 = {"hiz", 21, True, 20, "female"}
print(set1)     #Set yang berisi nilai string, int, boolean

myset = {"Belanda", "Italia", "Turki"}
print(type(myset))      #Melihat tipe data

thisset = set(("India", "Pakistan", "Palestina"))
print(thisset)      #Konstruktor set

#Mengakses item pada set
thisset = {"Turki", "Singapura", "Malaysia"}
for x in thisset:
  print(x)      #for loop

thisset = {"India", "Turki", "Kamboja"}
print("India" in thisset)   #Apakah ada India di set

thisset = {"India", "Turki", "Kamboja"}
print("India" not in thisset)   #Apakah tidak ada India di Set

#Add item set
thisset = {"Korea", "Korut", "China"}
thisset.add("Jepang")
print(thisset)

thisset = {"Korea", "Korut", "Jepang"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"India", "Turki", "Pakistan"}
mylist = ["kamboja", "Philipina"]
thisset.update(mylist)
print(thisset)

#Menghapus item
thisset = {"Jepang", "China", "Korut"}
thisset.remove("Korut")
print(thisset)

thisset = {"Turki", "Dubai", "Arab"}
x = thisset.pop()
print(x)
print(thisset) 

#Loop set
thisset = {"Indonesia", "Singapura", "Malaysia"}
for x in thisset:
  print(x)

#Gabungkan set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#Fozenset
x = frozenset({"Korea", "China", "Jepang"})
print(x)
print(type(x)) 


