katalog = [
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

riwayat_transaksi = set()

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    buku_ketemu = False
    
    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():
            buku_ketemu = True
            
            if buku['stok'] >= jumlah_beli:
                harga_total = buku['harga'] * jumlah_beli
                buku['stok'] -= jumlah_beli
                
                riwayat_transaksi.add(buku['nama'])
                
                print(f"Telah berhasil membeli buku '{buku['nama']}' sebanyak {jumlah_beli} buku | Total bayar: Rp {harga_total}")
            else:
                print(f"PERINGATAN: Stok '{buku['nama']}' nggak mencukupi (Sisa: {buku['stok']} stok) saja!")
            break

    if not buku_ketemu:
        print(f"ERROR: Buku '{nama_buku}' nggak ada di katalog!")

print("=== Selamat datang di PyBook Store ===\n")

print("=== Transaksi 1 ===")
proses_transaksi(katalog, "Belajar Python", 1)

print("\n=== Transaksi 2 ===")
proses_transaksi(katalog, "Belajar Python", 2)

print("\n=== Transaksi 3 ===")
proses_transaksi(katalog, "Struktur data", 12)

print("\n=== Daftar buku yang pernah dibeli ===")
for buku in riwayat_transaksi:
    print(" 1. " + buku)
    