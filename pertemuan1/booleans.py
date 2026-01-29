#Python Booleans
#Nilai Boolean
print(12 > 8)
print(12 == 8)
print(12 < 8)

a = 100
b = 40

if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

#Mengevaluasi Nilai dan Variabel
print(bool("Halo"))
print(bool(17))

x = "Halo"
y = 17

print(bool(x))
print(bool(y))

#Sebagian besar nilai adalah benar
print(bool("hij"))
print(bool(567))
print(bool(["Hera", "Wati", "Siregar"]))

#Beberapa Nilai Salah
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myhouse():
  def __len__(self):
    return 0

mycar = myhouse()
print(bool(mycar))

#Fungsi dapat Mengembalikan Nilai Boolean
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("Yeah!")
else:
  print("Tidak!")

  x = 4
print(isinstance(x, int)) #return True

x = 4.1
print(isinstance(x, int)) #return False
