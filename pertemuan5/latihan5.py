#Soal 1
stok_barang = [15, 40, 30, 10, 25]
stok_barang[3] = 50
print(stok_barang)

stok_barang.append(5)
print(stok_barang)
stok_barang.sort(reverse = True)
print(stok_barang)

print(sum(stok_barang))
rata = sum(stok_barang) /len(stok_barang)
print(True) if rata >= 20 else print(False)

#Soal 2
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for i in range (len(data_aktivitas)) :
    if data_aktivitas[i] [1] > 80:
        print(f"{data_aktivitas[i][0]} Mendapat peringkat Gold")
    elif 50 <= data_aktivitas[i][1] <= 80:
        print(f"{data_aktivitas[i][0]} Mendapat peringkat Silver")
    else :
        print(f"{data_aktivitas[i][0]} Mendapat peringkat Bronze")


#Soal 3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
print(ukm_coding - ukm_robotik)
print(ukm_coding | ukm_robotik)
print(True) if 'Andi' in ukm_robotik else print(False)

#Soal 4
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]

gudang_pc[1]['Kategori'] = 'Aksesoris'
print(gudang_pc)

gudang_pc.append({"item": "Headset",
                 'harga': 350000,
                 'stok': 20})
print(gudang_pc)

for i in range(len(gudang_pc)) :
    print(f"item: {gudang_pc[i]['item']} Total Aset: Rp {gudang_pc[i]['harga']*gudang_pc[i]['stok']}")
