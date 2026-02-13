#list 

#Menambah nilai 95
nilai = [75, 80, 65, 90, 85]
nilai.append(95)
print(nilai)

#Menghapus nilai terkecil
nilai = [75, 80, 65, 90, 85]
nilai.remove(65)
print(nilai)

#Mengurutkan list dari terkecil ke terbesar
nilai.sort()
print(nilai)

#Menampilkan nilai tertinggi, nilai terendah, jumlah data
nilai = [75, 80, 85, 90]
print(nilai[len(nilai)-1])
print(nilai[0])
print(len(nilai))

#Hitung rata-rata nilai setelah semua perubahan
nilai = [75, 80, 85, 90]
rata = 0
for l in nilai:
    rata += l
    

#Tampilkan seluruh isi list setelah diproses
nilai = [75, 80, 85, 90]
print(nilai)


