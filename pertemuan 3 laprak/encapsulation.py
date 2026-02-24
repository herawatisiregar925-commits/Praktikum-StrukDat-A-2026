#Properti Pribadi
class Teknik:
  def __init__(self, nama, nim):
    self.nama = nama
    self.__nim = nim  
    
p1 = Teknik("Herawati", 25071206988)
print(p1.nama)
print(p1.__nim) #ini akan error karna nim telah menjadi properti privat.

#Mengakses nilai properti yang telah diprivat
class Teknik:
  def __init__(self, nama, nim):
    self.nama = nama
    self.__nim = nim  
    
  def get_nim(self):
    return self.__nim

p1 = Teknik("Helena", 24071101)
print(p1.get_nim())

#Tetapkan Nilai Properti Pribadi
class Teknik:
  def __init__(self, nama, umur):
    self.nama = nama
    self.__umur = umur

  def get_umur(self):
    return self.__umur

  def set_umur(self, umur):
    if umur > 0:
      self.__umur = umur
    else:
      print("Umur yang panjang")

p1 = Teknik("Agustian", 19)
print(p1.get_umur())

p1.set_umur(27)
print(p1.get_umur())

#Encapsulation melindungi data
class Mahasiswa:
  def __init__(self, nama):
    self.nama = nama
    self.__nilai = 0

  def set_nilai(self, nilai):
    if 0 <= nilai <= 100:
      self.__nilai = nilai
    else:
      print("Nilai harus antara 0 sampai 100.")

  def get_nilai(self):
    return self.__nilai

  def get_status(self):
    if self.__nilai >= 60:
      return "Lulus"
    else:
      return "Tidak lulus"

mahasiswa = Mahasiswa("Hera")
mahasiswa.set_nilai(96)
print(mahasiswa.nama)
print(mahasiswa.get_nilai())
print(mahasiswa.get_status())

#Metode privat
class Kalkulator:
  def __init__(self):
    self.hasil = 0

  def __validasi(self, no):
    if not isinstance(no, (int, float)):
      return False
    return True

  def tambah(self, no):
    if self.__validasi(no):
      self.hasil += no
    else:
      print("Nomor tidak valid")

kalk = Kalkulator()
kalk.tambah(16)
kalk.tambah(12)
print(kalk.hasil)
