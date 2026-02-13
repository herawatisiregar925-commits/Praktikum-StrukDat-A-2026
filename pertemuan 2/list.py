#Membuat list
film = ["Dokumenter", "Action", "Horor"]
print(film)

#Allow duplicates (List dapat memiliki item yang sama)
film = ["Dokumenter", "Action", "Horor", "Action"]
print(film)

#Menghitung berapa banyak item di dalam sebuah list
film = ["Dokumenter", "Action", "Horor"]
print(len(film))

#Item dalam list dapat berupa tipe data apa pun
daftar1 = ["Dokumenter", "Action", "Horor"]
daftar2 = [1, 2, 4, 8, 11]
daftar3 = [False, True, True]

print(daftar1)
print(daftar2)
print(daftar3)

#List yang berisi nilai string, integer, dan boolean sekaligus
film = ["Action", 12, True, 16, "male"]
print(film)

#Mengonfirmasi bahwa  berasal dari kelas <class 'list'>
film = ["Dokumenter", "Action", "Horor"]
print(type(film))

#Membuat list baru dengan konstruktor list()
film = list(("Drama", "Romcom", "Thriller"))
print(film)

#Mengakses item list
film = ["Dokumenter", "Action", "Horor"]
print(film[1])

#Pengindeksan negatif
film = ["Dokumenter", "Action", "Horor"]
print(film[-3])

#Rentang indeks
film = ["Dokumenter", "Action", "Horor", "Romcom", "Thriller", "Historical"]
print(film[2:4])

film = ["Dokumenter", "Action", "Horor", "Romcom", "Thriller", "Historical"]
print(film[:4])

film = ["Dokumenter", "Action", "Horor", "Romcom", "Thriller", "Historical"]
print(film[2:])

#Rentang indeks negatif
film = ["Dokumenter", "Action", "Horor", "Romcom", "Thriller", "Historical"]
print(film[-4:-1])

#Memeriksa apakah item ada pada list
film = ["Dokumenter", "Action", "Horor", "Romcom", "Thriller", "Historical"]
if "Action" in film:
  print("Yaa, 'Action' ada di list film")

#Mengubah nilai item
film = ["Dokumenter", "Action", "Horor"]
film[1] = "Thriller"
print(film)

#Mengubah Rentang Nilai Item
film = ["Dokumenter", "Action", "Horor"]
film[1:3] = ["Thriller", "Romcom"]
print(film)

film = ["Dokumenter", "Action", "Horor"]
film[1:2] = ["Thriller", "Romcom"]  #Mengubah nilai kedua dengan menggantinya dengan dua nilai baru
print(film)

film = ["Dokumenter", "Action", "Horor"]
film[1:3] = ["Thriller"]	#Mengubah nilai kedua dan ketiga dengan menggantinya dengan satu nilai
print(film)

film = ["Dokumenter", "Action", "Horor"]
film.insert(2, "Thriller")	#Metode insert() menyisipkan item pada indeks yang ditentukan
print(film)

#Menambah item ke list (di bagian akhir)
film = ["Dokumenter", "Action", "Horor"]
film.append("Komedi")
print(film)

#Memperluas list
film = ["Dokumenter", "Action", "Horor"]
music = ["Kpop", "Pop", "Jazz"]
film.extend(music)      #Menambahkan item dari list lain ke list sekarang
print(film)

film = ["Dokumenter", "Action", "Horor"]
music = ("Kpop", "Pop", "Jazz")     #Menambahkan objek iterable tuple
film.extend(music)
print(film)

#Menghapus item yang ditentukan
film = ["Dokumenter", "Action", "Horor"]
film.remove("Horor")
print(film)

#Menghapus indeks yang ditentukan
film = ["Dokumenter", "Action", "Horor"]
film.pop(1)
print(film)

#Menghapus item terakhir
film = ["Dokumenter", "Action", "Horor"]
film.pop()
print(film)

#Menghapus indeks yang ditentukan
film = ["Dokumenter", "Action", "Horor"]
del film[1]
print(film)

#Menghapus list seluruhnya
film = ["Dokumenter", "Action", "Horor"]
del film
print(film)

#Mengosongkan list
film = ["Dokumenter", "Action", "Horor"]
film.clear()
print(film)

#Loop melalui list
film = ["Dokumenter", "Action", "Horor"]
for x in film:
  print(x)

#Loop melalui nomor indeks
film = ["Dokumenter", "Action", "Horor"]
for i in range(len(film)):
  print(film[i])

#Loop while
film = ["Dokumenter", "Action", "Horor"]
i = 0
while i < len(film):
  print(film[i])
  i = i + 1

#Loop melalui List Comprehension
film = ["Dokumenter", "Action", "Horor"]
[print(x) for x in film]

#List comprehension
film = ["Dokumenter", "Action", "Horor"]
newlist = [x for x in film if "A" in x]
print(newlist)

film = ["Dokumenter", "Action", "Horor"]
newlist = [x for x in film if x != "Action"]
print(newlist)

#Dapat diulang
newlist = [x for x in range(10) if x < 7]
print(newlist)

#Ekspresi
film = ["Dokumenter", "Action", "Horor"]
newlist = ['holla' for x in film]
print(newlist)

film = ["Dokumenter", "Action", "Horor"]
newlist = [x if x != "Horor" else "Thriller" for x in film]
print(newlist)

#Sort list
#Urutkan Daftar Secara Alfanumerik
film = ["Dokumenter", "Action", "Horor"]
film.sort()		#Mengurutkan list secara alfabetis
print(film)

thislist = [100, 50, 200, 250, 150]
thislist.sort()		#Mengurutkan list secara numerik
print(thislist)

#Urutkan menurun
film = ["Dokumenter", "Action", "Horor"]
film.sort(reverse = True)		#Mengurutkan list secara menurun
print(film)

thislist = [100, 50, 200, 250, 150]
thislist.sort(reverse = True)		#Mengurutkan list secara menurun
print(thislist)

#Sesuaikan Fungsi Pengurutan
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Pengurutan Peka Huruf Besar/Kecil
film = ["dokumenter", "Action", "horor", "Romcom"]
film.sort()
print(film)
#Pengurutan Tidak Peka Huruf Besar/Kecil
film = ["dokumenter", "action", "Horor", "Romcom"]
film.sort(key = str.lower)
print(film)

#Membalikkan Urutan
film = ["dokumenter", "action", "Horor", "Romcom"]
film.reverse()
print(film)

#Copy List
film = ["Dokumenter", "Action", "Horor"]
myfilm = film.copy()      #Pakai metode copy()
print(myfilm)

film = ["Dokumenter", "Action", "Horor"]
myfilm = list(film)        #Pakai metode list()
print(myfilm)

film = ["Dokumenter", "Action", "Horor"]
myfilm = film[:]          #Pakai operator :
print(myfilm)

#Menggabungkan Dua Daftar
list1 = ["Avatar", "Barbie", "Cinderella"]
list2 = [1, 2, 3]
list3 = list1 + list2     #Pakai operator +
print(list3)

list1 = ["Avatar", "Barbie", "Cinderella"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)         #Pakai metode .append()
print(list1)

list1 = ["Avatar", "Barbie", "Cinderella"]
list2 = [1, 2, 3]
list1.extend(list2)       #Pakai metode .extend()
print(list1)





