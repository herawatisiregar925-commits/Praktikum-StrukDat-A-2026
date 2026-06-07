katalog = [ 
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
] 

def cari_buku(katalog, keyword):
    hasil_cari = []
    
    keyword = keyword.lower()
    
    for buku in katalog:
        if keyword in buku['nama'].lower():
            hasil_cari.append(buku)

    if len(hasil_cari) == 0:
        print("\nBuku tidak ditemukan.")  
    return hasil_cari

print("=== Pencarian Buku PyBook Store ===")
kata_kunci = input("Masukkan kata kunci buku yang sedang kamu cari: ")

hasil = cari_buku(katalog, kata_kunci)

if len(hasil) > 0:
    print(f"\nHasil ditemukan {len(hasil)} buku yang cocok:")
    for buku in hasil:
        print(f"Nama buku   : {buku['nama']}")
        print(f"Harga buku  : Rp {buku['harga']}")
        print(f"Stok  buku  : {buku['stok']}")
