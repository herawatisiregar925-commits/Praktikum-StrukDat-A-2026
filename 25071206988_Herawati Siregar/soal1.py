def tambah_buku(nama, harga, stok):
    if harga <= 0 or stok < 0:
        print("ERROR: Harga harus > 0 dan stok tidak boleh negatif!")
        return None
    
    data = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }
    return data

list_buku = []

print("=== Input Data Buku ===")
for i in range(3):
    print(f"\nMasukkan buku ke-{i+1}")
    nama = input("Nama buku:  ")
    harga = float(input("Harga buku: "))
    stok = int(input("Stok buku:  "))
    
    hasil = tambah_buku(nama, harga, stok)
    if hasil != None:
        list_buku.append(hasil)

print("\n=== Data daftar buku yang berhasil ditambahkan ===")
for buku in list_buku:
    print(f"Nama buku: {buku['nama']}, Harga buku: Rp {buku['harga']}, Stok buku: {buku['stok']}")
    