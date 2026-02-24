#Membuat kelas Induk
class Teknik:
  def __init__(self, namdep, nambel):
    self.namadepan = namdep
    self.namabelakang = nambel

  def printnama(self):
    print(self.namadepan, self.namabelakang)

x = Teknik("Herawati", "Siregar")
x.printnama()

#Membuat kelas turunan
class Teknik:
  def __init__(self, namdep, nambel):
    self.namadepan = namdep
    self.namabelakang = nambel

  def printnama(self):
    print(self.namadepan, self.namabelakang)

class Mahasiswa(Teknik):
  pass

x = Mahasiswa("Yazid", "Siregar")
x.printnama()

#Menambahkan fungsi __init__( )
class Teknik:
  def __init__(self, namdep, nambel):
    self.namadepan = namdep
    self.namabelakang = nambel

  def printnama(self):
    print(self.namadepan, self.namabelakang)

class Mahasiswa(Teknik):
  def __init__(self, namdep, nambel):
    Teknik.__init__(self, namdep, nambel)

x = Mahasiswa("Fairuz", "Siregar")
x.printnama()

#Menggunakan fungsi super()
class Teknik:
  def __init__(self, namdep, nambel):
    self.namadepan = namdep
    self.namabelakang = nambel

  def printnama(self):
    print(self.namadepan, self.namabelakang)

class Mahasiswa(Teknik):
  def __init__(self, namdep, nambel):
    super().__init__(namdep, nambel)

x = Mahasiswa("Kim", "Mingyu")
x.printnama()

#Menambahkan Properti
class Teknik:
  def __init__(self, namdep, nambel):
    self.namadepan = namdep
    self.namabelakang = nambel

  def printnama(self):
    print(self.namadepan, self.namabelakang)

class Mahasiswa(Teknik):
  def __init__(self, namdep, nambel, tahun):
    super().__init__(namdep, nambel)
    self.tahunlulus = tahun

x = Mahasiswa("Kim", "Mingyu", 2028)
print(x.tahunlulus)

#Menambahkan metode
class Teknik:
  def __init__(self, namdep, nambel):
    self.namadepan = namdep
    self.namabelakang = nambel

  def printnama(self):
    print(self.namadepan, self.namabelakang)

class Mahasiswa(Teknik):
  def __init__(self, namdep, nambel, tahun):
    super().__init__(namdep, nambel)
    self.tahunlulus = tahun

  def welcome(self):
    print("Selamat datang", self.namadepan, self.namabelakang, "ke wisuda tahun", self.tahunlulus)

x = Mahasiswa("Herawati", "Siregar", 2028)
x.welcome()
