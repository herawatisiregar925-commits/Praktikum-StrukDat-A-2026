class HashTable:
    """Membuat hash table dengan 10 bucket. Setiap bucket berupa list kosong"""
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def hash_funct(self, kode):
        #Menjumlahkan Unicode tiap karakter
        total = 0
        for char in str(kode):
            total += ord(char)
        return total % self.size
    
    def insert(self, kode, judul):
        """Menambahkan buku baru, update buku jika kode sudah ada"""
        index = self.hash_funct(kode) #Cari index bucket
        bucket = self.table[index] #Ambil bucket pada index
        for i, (k, j) in enumerate(bucket): #Pengecekkan apakah kode sudah ada
            if k == kode: #Jika kode ditemukan
                #Update buku setelah kode ada
                bucket[i] = (kode, judul)
                print(f"Data dengan kode '{kode}' berhasil di-update!!")
                return
        bucket.append((kode, judul)) #Menambahkan data jika kosong
        print(f"Data '{kode}' : '{judul}' berhasil ditambahkan!")
    
    def search(self, kode):
        """Menampilkan judul buku berdasarkan kode. Jika buku tidak ditemukan maka tampilkan pesan “Buku tidak ditemukan” """
        index = self.hash_funct(kode) #Cari index bucket
        bucket = self.table[index] #Ambil bucket pada index
        for k, j in bucket: #Cari kode di bucket
            if k == kode:
                return j
        return "Buku tidak ditemukan" #Jika tidak ditemukan
    
    def delete(self, kode):
        """Menghapus buku berdasarkan kode"""
        index = self.hash_funct(kode) #Cari index bucket
        bucket = self.table[index] #Ambil bucket pada index
        for i, (k, j) in enumerate(bucket): #Cari posisi data
            if k == kode:
                del bucket[i] #Hapus data
                print(f"Data dengan kode '{kode}' berhasil di hapus!!")
                return True
        print(f"Kode {kode} tidak ditemukan!") #Jika kode tidak dtemukan
        return False
    
    def display(self):
        """Menampilkan seluruh isi hash table"""
        print("\n========== ISI DATA BUKU DI PERPUSTAKAAN ===========")

        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")
        
        print("====================================================\n")
    
ht = HashTable()

print("\n=================")
print("Insert Data Buku: ")
print("=================")
ht.insert("BK111", "Mahir C++ Dalam Satu Jam")
ht.insert("BK222", "Python Dasar")
ht.insert("BK333", "Matematika Diskrit")
ht.insert("BK444", "Atomic Habits")
ht.insert("BK555", "Kalkulus")
ht.insert("BK666", "Mahir UI/UX Pemula")
ht.insert("BK777", "Struktur Data")

print("\n==========================")
print("Display Data Buku Terkini: ")
print("==========================")
ht.display()

print("\n=================")
print("Insert Data Buku: ")
print("=================")
ht.insert("BK045", "Mein Kampf")
ht.insert("BK111", "Bumi Manusia")

print("\n==========================")
print("Display Data Buku Terkini: ")
print("==========================")
ht.display()

print("\n====================")
print("Pencarian Data Buku: ")
print("====================")
print("Masukkan kode buku yang kamu cari:", ht.search("BK666"))
print("Masukkan kode buku yang kamu cari:", ht.search("BK1286"))

print("\n================")
print("Hapus Data Buku: ")
print("================")
ht.delete("BK444")

print("\n==========================")
print("Display Data Buku Terkini: ")
print("==========================")
ht.display()