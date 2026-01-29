#Python Data Types

#Tipe Data Bawaan
#Python memiliki tipe data bawaan berikut secara default, dalam kategori-kategori ini:
"""
Text Type: str
Numeric Types: int, float, complex
Sequence Types:	list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes,bytearray, memoryview
None Type: NoneType
"""

#Mendapatkan Tipe Data
#Anda dapat memperoleh tipe data dari objek apa pun dengan menggunakan type()fungsi berikut:
x = 100
print(type(x))

#Mengatur Tipe Data
#Dalam Python, tipe data ditentukan saat Anda memberikan nilai ke sebuah variabel:
x = "Halo Semua"	#str	
x = 100	#int	
x = 3.5	#float	
x = 1j	#complex	
x = ["Hera", "Wati", "Siregar"]	#list	
x = ("Korea", "Dubai", "Makkah")	#tuple	
x = range(4)	#range	
x = {"name" : "Hera", "age" : 20}	#dict	
x = {"Kamar", "Dapur", "Toilet"}	#set	
x = frozenset({"FT", "FMIPA", "FH"})	#frozenset	
x = True	#bool	
x = b"Holla"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

#Menetapkan Tipe Data Spesifik
#Jika Anda ingin menentukan tipe data, Anda dapat menggunakan fungsi konstruktor berikut:
x = str("Halo Semua")	#str	
x = int(100)	#int	
x = float(3.5)	#float	
x = complex(1j)	#complex	
x = list(("Hera", "Wati", "Siregar"))	#list	
x = tuple(("Korea", "Dubai", "Makkah"))	#tuple	
x = range(4)	#range	
x = dict(name="Hera", age=20)	#dict	
x = set(("Kamar", "Dapur", "Toilet"))	#set	
x = frozenset(("FT", "FMIPA", "FH")) #frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
