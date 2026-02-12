class Person :
    def __init__(self, nama, jenisKelamin, umur):
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.umur = umur

class Karyawan(Person):
    def __init__(self, nama, jenisKelamin, umur, gaji):
        super().__init__(nama, jenisKelamin, umur)
        self._gaji = gaji  #Protected
    
    def get_gaji(self):
        return self._gaji

class Rekening :
    def __init__(self, noRekening, PIN):
        self.noRekening = noRekening
        self.__PIN = PIN
    
    def get_PIN(self):
        return self.__PIN
    
    def set_PIN(self, newPin):
        self.__newPin = newPin

p1 = Karyawan("Hera", "Perempuan", 19, 20000000)
r1 = Rekening("1286", "1144")

print(r1.get_PIN())
print(p1.nama)
print(p1.get_gaji())

    
    


