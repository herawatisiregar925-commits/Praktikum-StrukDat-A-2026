#Python Variables

#Membuat Variabel
x = 100
y = "Herawati Siregar"
print(x)
print(y)

x = 12       # x sekarang adalah int
x = "Heraa" # x sekarang menjadi str
print(x)

#Casting
x = str(12)    # x akan menjadi '12'
y = int(12)    # y akan menjadi 12
z = float(12)  # z llakan menjadi 12.0

print(x)
print(y)
print(z)

#Mendapatkan tipe
x = 12
y = "Herawati Siregar"
print(type(x))
print(type(y))

#Tanda kutip tunggal atau ganda
x = "Mingyu pergi ke konser"
print(x)
#Variabel string dapat dideklarasikan dengan menggunakan tanda kutip tunggal atau ganda:
x = 'Mingyu pergi ke konser'
print(x)

#Peka terhadap Huruf Besar/Kecil
a = 16
A = "Mingyu pergi ke Paris"
#A tidak akan menimpa a

print(a)
print(A)

#Python - Variable Names

#Nama Variabel
myvar = "Hera"
my_var = "Lulus"
_my_var = "Cumlaude"
myVar = "Dan"
MYVAR = "Tepat"
myvar2 = "Waktu"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Nama Variabel Multi Kata

#Camel Case
myVariableName = "Hera"

#Pascal Case
MyVariableName = "Wati"

#Snake Case
my_variable_name = "Siregar"

#Python Variables - Assign Multiple Values

#Banyak Nilai untuk Banyak Variabel
x, y, z = "Mingyu", "Hera", "Oliver"

print(x)
print(y)
print(z)

#Satu Nilai untuk Beberapa Variabel
x = y = z = "Cumlaude"
print(x)
print(y)
print(z)

#Membuka Koleksi
Kpop = ["Seventeen", "Blackpink", "Cortis"]
x, y, z = Kpop

print(x)
print(y)
print(z)

#Python - Output Variables
x = "Mingyu suka kimchi"
print(x)

x = "Mama"
y = "pergi"
z = "ke Mall"
print(x, y, z)

x = "Fakultas "
y = "Teknik "
z = "Unri"
print(x + y + z)

x = 99
y = 1
print(x + y)

x = 100
y = "Summa Cumlaude"
print(x, y)

#Python - Global Variables
x = "Keren"

def myfunc():
  print("Fakultas teknik sangat " + x)

myfunc()

x = "menarik"

def myfunc():
  x = "keren"
  print("Pemrograman sangat " + x)

myfunc()

print("Struktur data sangat " + x)

#Kata kunci global
def myfunc():
  global x
  x = "sukses"

myfunc()

print("Universitas Riau " + x)

x = "hebat"

def myfunc():
  global x
  x = "terdepan"

myfunc()

print("Universitas Riau " + x)
