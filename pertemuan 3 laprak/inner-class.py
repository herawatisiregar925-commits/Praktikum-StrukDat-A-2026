#Membuat Kelas Dalam Python
class Luar:
  def __init__(self):
    self.nama = "Outer Class"

  class Dalam:
    def __init__(self):
      self.nama = "Inner Class"

    def display(self):
      print("This is the inner class")

luar = Luar()
print(luar.nama)

#Mengakses Kelas Dalam dari Luar
class Luar:
  def __init__(self):
    self.nama = "Outer"

  class Dalam:
    def __init__(self):
      self.nama = "Inner"

    def display(self):
      print("Hello dari inner class")

luar = Luar()
dalam = luar.Dalam()
dalam.display()

#Mengakses Kelas Luar dari Dalam
class Luar:
  def __init__(self):
    self.nama = "Hera"

  class Dalam:
    def __init__(self, luar):
      self.luar = luar

    def display(self):
      print(f"Nama kelas luar: {self.luar.nama}")

luar = Luar()
dalam = luar.Dalam(luar)
dalam.display()

#Beberapa Kelas Dalam
class Komputer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def proses(self):
      print("Memproses data...")

  class RAM:
    def penyimpan(self):
      print("Penyimpanan data...")

komputer = Komputer()
komputer.cpu.proses()
komputer.ram.penyimpan()
