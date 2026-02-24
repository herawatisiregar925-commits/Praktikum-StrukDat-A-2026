#Polimorfisme Fungsi
#String
x = "Haloo Herawati!"
print(len(x))

#Tuple
mytuple = ("FT", "FMIPA", "FH", "FEB", "FISIP")
print(len(mytuple))

#Dictionary
thisdict = {
  "fakultas": "Teknik",
  "prodi": "TI",
  "tahun": 2028
}

print(len(thisdict))

#Polimorfisme Kelas
class Mobil:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def gerak(self):
    print("Mengendarai!")

class Sepeda:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def gerak(self):
    print("Mengayuh!")

class Pesawat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def gerak(self):
    print("Menerbangi!")

mobil1 = Mobil("Ferrari", "F1")       
sepeda1 = Sepeda("Polygon", "Sepeda Gunung") 
pesawat1 = Pesawat("Jet", "12168")     

for x in (mobil1, sepeda1, pesawat1):
  x.gerak()
