#Membuat Tuple
kendaraan = ("Mobil", "Sepeda motor", "Sepeda")
print(kendaraan)

#Panjang Tuple
kendaraan = ("Mobil", "Sepeda motor", "Sepeda")
print(len(kendaraan))

#Buat Tuple dengan Satu Item
kendaraan = ("Mobil",)
print(type(kendaraan))

#Item Tuple
tuple1 = ("Mobil", "Sepada motor", "Sepeda")
tuple2 = (1, 3, 5, 7, 9)
tuple3 = (True, True, False)

print(tuple1)
print(tuple2)
print(tuple3)

#Tuple bernilai string, integer, boolean
tuple1 = ("Mobil", 20, True, 100, "Perempuan")
print(tuple1)

#Tipe tuple
kendaraan = ("Mobil", "Sepeda motor", "Sepeda")
print(type(kendaraan))

#Konstruktor tuple()
kendaraan = tuple(("Mobil", "Sepeda motor", "Sepeda"))
print(kendaraan)

#Mengakses item tuple
kendaraan = ("Mobil", "Sepeda motor", "Sepeda")
print(kendaraan[1])

#Pengindeksan negatif
kendaraan = ("Mobil", "Sepeda motor", "Sepeda")
print(kendaraan[-1])

#Rentang indeks
kendaraan = ("Mobil", "Sepeda motor", "Sepeda")
print(kendaraan[1:3])

#Periksa item apakah ada
kendaraan = ("Mobil", "Sepeda motor", "Sepeda")
if "Sepeda" in kendaraan:
  print("Yaa, 'Sepeda' ada di tuple kendaraan")

#Memperbarui nilai tuple
x = ("Mobil", "Sepeda motor", "Sepeda")
y = list(x)
y[1] = "Pesawat"
x = tuple(y)
print(x)

thistuple = ("Mobil", "Pesawat", "Sepeda")
y = list(thistuple)
y.append("Helikopter")
thistuple = tuple(y)
print(thistuple)

#Menambahkan tuple ke tuple
thistuple = ("Mobil", "Pesawat", "Helikopter")
y = ("Jet sky",)
thistuple += y          
print(thistuple)

#Menghapus item
thistuple = ("Pesawat", "Mobil", "Kapal")
y = list(thistuple)
y.remove("Mobil")
thistuple = tuple(y)
print(thistuple)

#Unpack Tuple (Menguraikan)
kendaraan = ("Mobil", "Kapal", "Helikopter")
(green, yellow, red) = kendaraan
print(green)
print(yellow)
print(red)

#Menggunakan Asterisk*
kendaraan = ("Mobil", "Pesawat", "Kapal", "Helikopter", "Sepeda")
(green, yellow, *red) = kendaraan
print(green)
print(yellow)
print(red)

kendaraan = ("Mobil", "Pesawat", "Kapal", "Helikopter", "Sepeda")
(green, *tropic, red) = kendaraan
print(green)
print(tropic)
print(red)

#Perulangan tuple
kendaraan = ("Mobil", "Pesawat", "Helikopter")
for x in kendaraan:
  print(x)

#Perulangan melalui nomor indeks
kendaraan = ("Mobil", "Pesawat", "Helikopter")
for i in range(len(kendaraan)):
  print(kendaraan[i])

#Perulangan melalui Loop while
kendaraan = ("Mobil", "Pesawat", "Helikopter")
i = 0
while i < len(kendaraan):
  print(kendaraan[i])
  i = i + 1

#Join Tuple
#Gabungkan Dua Tuple
tuple1 = ("Mobil", "Sepeda" , "Pesawat")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Mengalikan Tuple
kendaraan = ("Mobil", "Pesawat", "Sepeda")
mytuple = kendaraan * 2

print(mytuple)
