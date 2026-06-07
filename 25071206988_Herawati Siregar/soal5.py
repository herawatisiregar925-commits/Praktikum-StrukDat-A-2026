katalog = [ 
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
] 

log_transaksi = []

def tambah_buku(nama, harga, stok):
    if harga <= 0 or stok < 0:
        print("ERROR: Harga harus > 0 dan stok tidak boleh negatif!")
        data = {"nama": nama,"harga": harga,"stok": stok}
    return data
