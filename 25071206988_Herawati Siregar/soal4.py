level_diskon = ( 
    (500000, 15),   # belanja >= 500.000 -> diskon 15% 
    (300000, 10),   # belanja >= 300.000 -> diskon 10% 
    (100000,  5),   # belanja >= 100.000 -> diskon  5% 
    (0,       0),  # default  -> tidak ada diskon      
) 
def hitung_diskon(total_belanja, level_diskon, index=0):
    belanja = level_diskon[index][0]
    persen_diskon = level_diskon[index][1]

    if  total_belanja >= belanja:
        nominal_diskon = (persen_diskon / 100) * total_belanja
        total_bayar = total_belanja - nominal_diskon
        return (persen_diskon, nominal_diskon, total_bayar)
    else:
        return hitung_diskon(total_belanja, level_diskon, index + 1)

print("=== Cek Diskon ===")
nama = input("Masukkan nama: ")
total = float(input("Masukkan total belanja: "))

hasil = hitung_diskon(total, level_diskon)
persen_disk, nominal_disk, total_akhir = hasil

print("\n=== Ringkasan Pembayaran ===")
print("Nama pembeli   :", nama)
print("Total belanja  : Rp", total)

if total < 100000:
    print("Tidak ada diskon.")
else:
    print("Persen diskon  :", persen_disk, "%")
    print("Nominal diskon : Rp", nominal_disk)

print("Total akhir    : Rp", total_akhir)
