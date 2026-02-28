import kurs as kurs

def konversi():
    try :
        kurs_awal = "".join(input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()).strip()
        kurs_tujuan = "".join(input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()).strip()
        jumlah = float(input("Jumlah: "))

        idr = jumlah * kurs.konversi_ke_idr[kurs_awal]
        hasil = idr / kurs.konversi_ke_idr[kurs_tujuan]
        print(f"{kurs.label_mata_uang[kurs_awal]} {jumlah} = {kurs.label_mata_uang[kurs_tujuan]} {hasil:.2f}")

    except KeyError : 
        print("Error: Kode mata uang tidak ditemukan!")
    except ValueError :
        print("Error: Masukkan angka valid pada jumlah.")

