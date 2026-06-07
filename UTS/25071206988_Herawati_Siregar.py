pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False}, 
]

print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
print(" No | ID   | Nama   | Usia | Kategori | Status Kembali ")

def tampilkan_pengunjung(data):
    for i in range(len(data)):
        print(f"{i+1} | ID {data[i]['id']} | Nama {data[i]['nama'].ljust(6)} | Usia {data[i]['usia']} | Kategori {data[i]['kategori']} | Status Kembali {data[i]['kembali']}")

tampilkan_pengunjung(pengunjung_hari_ini)

def filter_belum_kembali(data):
    total = 0
    belum_kembali = []
    for i in range(len(data)):
        if data[1]['Kembali'] == 0:
            total += 1
            belum_kembali.append(data[i]['nama'])
        else:
            pass

    belum_kembali.sort()
    for i in range(len(belum_kembali)):
        print(f"{i+1}', {belum_kembali[i]}")
        print(f"Total belum kembali: {total} pengunjung")
        return belum_kembali
    
    filter_belum_kembali(pengunjung_hari_ini)

#2
def info_perpustakaan(data):
    print("Info Perpustakaan: ")
    tetap = tuple(data)
    return tetap
def rekap_kategori(data):
    data_set = set(data)



#3 
class Pengunjung:
    def __init__(self, id, nama, kategori):
        self.id = id
        self.nama = nama
        self.kategori = kategori

class PengunjungPrioritas(Pengunjung):
    def __init__(self, prioritas, mendesak, biasa):
        self.prioritas = prioritas
        self.mendesak = mendesak
        self.biasa = biasa
#4
class Node:
  def __init__(self, data):
        self.data = data
        self.next = None
        data = {"id", "nama", "kategori"} 

class AntrianPeminjaman:
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_semua_pengunjung = []

    def tambah_data(self, nama, pengunjung, prioritas):
        baru = Pengunjung(nama, pengunjung, prioritas)
        node_baru = Node(baru)

        self.list_semua_pengunjung.append(pengunjung)

        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru
        print(f"Pengunjung {nama} berhasil didaftarkan.")

    def tampilkan(self):
        print("\n--- DAFTAR ANTRIAN SAAT INI ---")
        temp = self.head
        while temp:
            p = temp.data
            status = "Mendesak" if p.prioritas == 1 else "Biasa"
            print(f"Nama: {p.nama} | Prioritas: {p.prioritas} | Status: {status}")
            temp = temp.next

    def buat_rekapan(self):
        kategori_unik = set(self.list_semua_pengunjung)