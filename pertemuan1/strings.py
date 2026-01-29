#Python Strings

#Strings
#Anda dapat menggunakan tanda kutip ganda atau tunggal:
print("Heraa")
print('Heraa')

#Kutipan di Dalam Kutipan
print("It's okayyy")
print("Namaku 'Herawati'")
print('Panggilannya "Hera"')

#Menetapkan String ke Variabel
h = "Anggur"
print(h)

#String Multibaris
a = """Saya berkuliah di teknik Informatika,
yang merupakan salah satu prodi di Fakultas teknik Universitas Riau, 
prodi ini merupakan prodi ramai peminat pada SNBP 2025, 
Saya masuk melalui jalur SMBT UNRI karena belum beruntung pada saat SNBP dan SNBT di UNAND."""
print(a)

a = '''Saya berkuliah di teknik Informatika,
yang merupakan salah satu prodi di Fakultas teknik Universitas Riau, 
prodi ini merupakan prodi ramai peminat pada SNBP 2025, 
Saya masuk melalui jalur SMBT UNRI karena belum beruntung pada saat SNBP dan SNBT di UNAND.'''
print(a)

#String adalah Array
a = "Selamat pagi dunia!"
print(a[1])

#Melakukan perulangan melalui sebuah string
for x in "hera":
  print(x) 

#Panjang string
a = "Herawati Siregar"
print(len(a))

#Periksa String
txt = "Grand opening cafee itu minumannya free!"
print("free" in txt)

txt = "Grand opening cafee itu minumannya free!"
if "free" in txt:
  print("Ya, 'free' minumannya.")

#Periksa jika TIDAK
txt = "Grand opening cafee itu minumannya free!"
print("makanannya" not in txt)

txt = "Grand opening cafee itu minumannya free!"
if "makanannya" not in txt:
  print("Tidak, 'makanannya' tidak free.")

#Python - Slicing Strings

#Slicing
b = "Hera, Wati!"
print(b[2:5])

#Slice dari Awal
b = "Butuh, dana!"
print(b[:5])

#Slice Hingga Ujungnya
b = "Butuh, uang!"
print(b[2:])

#Pengindeksan Negatif
b = "Butuh, mobil!"
print(b[-5:-2])

#Python - Modify Strings

#Huruf besar
a = "Semangat, teman!"
print(a.upper())

#Huruf Kecil
a = "Semangat, teman!"
print(a.lower())

#Hapus Spasi Kosong
a = " Belajar, yaa! "
print(a.strip())

#Ganti String
a = "Belanja, baju!"
print(a.replace("B", "H"))

#Pisahkan String
a = "Pergi, ngampus!"
print(a.split(",")) # returns ['Pergi', ' ngampus!']

#Python - String Concatenation

#Penggabungan String
a = "Selamat"
b = "wisuda"
c = a + b
print(c)

#Untuk menambahkan spasi di antara keduanya, tambahkan tanda titik dua ( " ":).
a = "Selamat"
b = "wisuda"
c = a + " " + b
print(c)

#Python - Format - Strings

#F string
umur = 20
txt = f"Namaku Hera, Umurku {umur}"
print(txt)

#Placeholder dan Modifier
harga = 20
txt = f"Harga ayam geprek itu {harga} rupiah"
print(txt)

harga = 20
txt = f"Harga ayam geprek itu {harga:.2f} rupiah"
print(txt)

txt = f"Harga ayam geprek itu {2000 * 10} rupiah"
print(txt)

#Python - Escape Characters

#Karakter escape
txt = "Kami dikenal sebagai \"Panglima tempur\" dari Pekanbaru."
print(txt) 

txt = 'It\'s okayy.'
print(txt) #Single Quote

txt = "Jadi ini untuk garis miring contoh : mobil \\ motor (backslash)."
print(txt) #Backslash

txt = "Pagi\nHari!"
print(txt) #New Line

txt = "Siang\rHari!"
print(txt) #Carriage Return

txt = "Buah\tAnggur"
print(txt) #Tab

