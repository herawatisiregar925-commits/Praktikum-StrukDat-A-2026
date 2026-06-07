#Node untuk menampung data setiap pasien
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None  # Pointer ke pasien di belakangnya

#Struktur data Queue menggunakan konsep Linked List manual.
class QueueRumahSakit:
    def __init__(self):
        self.head = None    #Pasien paling depan (Pertama dipanggil)
        self.tail = None    #Pasien paling belakang (Terakhir dipanggil)
        self._size = 0      #Menghitung jumlah pasien
        self.nomor_antrian = 0

    #1. Enqueue: Mendaftarkan pasien baru ke antrian (di bagian belakang/tail)
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)

        self.nomor_antrian += 1

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.nomor_antrian})")

    #2. Dequeue: Memanggil dan mengeluarkan pasien paling depan (head)
    def dequeue(self):
        if self.is_empty():
            print("[PERINGATAN] Antrian kosong, tidak ada pasien untuk dipanggil.")
            return None
        
        temp = self.head
        self.head = self.head.next
        self._size -= 1
        
        #Setelah digeser head jadi None, maka antrian kosong (tail juga harus None)
        if self.head is None:
            self.tail = None
            
        print(f"[PANGGIL] Dokter memanggil: {temp.nama} (keluhan: {temp.keluhan})")
        return temp

    #3. Peek: Melihat pasien paling depan tanpa mengeluarkannya
    def peek(self):
        if self.is_empty():
            return None
        print(f"[PEEK] Pasien berikutnya: {self.head.nama} — {self.head.keluhan}")
        return self.head

    #4. Is_empty: Mengecek apakah antrian kosong
    def is_empty(self):
        return self.head is None

    #5. Size: Menghitung jumlah pasien
    def size(self):
        return self._size

    #6. Clear: Mengosongkan seluruh antrian
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    #Menampilkan seluruh isi antrian saat ini
    def tampilkan_antrian(self):
        print("[ANTRIAN SAAT INI]")
        if self.is_empty():
            print("Antrian kosong.")
            return
        
        current = self.head
        no = 1
        while current is not None:
            print(f"{no}. {current.nama} → {current.keluhan}")
            current = current.next
            no += 1

# SKENARIO PENGUJIAN (Main Program)

if __name__ == "__main__":
    def main():
        print("======================================")
        print("      SISTEM ANTRIAN POLI UMUM      ")
        print("          RS Sehat Bersama          ")
        print("======================================\n")

    poli_umum = QueueRumahSakit()
    main()

    #Cek apakah antrian kosong
    status = "YA, antrian masih kosong." if poli_umum.is_empty() else "TIDAK, ada pasien."
    print(f"[CEK] Apakah antrian kosong? → {status}")
    print("\n")

    #Pendaftaran pasien
    poli_umum.enqueue("Budi", "Demam tinggi")
    poli_umum.enqueue("Ani", "Batuk pilek")
    poli_umum.enqueue("Citra", "Sakit kepala")
    print("\n")

    #Jumlah pasien yang nunggu
    print(f"[INFO] Jumlah pasien menunggu: {poli_umum.size()} orang")

    #Cek pasien berikutnya (peek)
    poli_umum.peek()
    print("\n")

    #Dokter memanggil pasien pertama (dequeue)
    poli_umum.dequeue()

    #Pasien DODI mendaftar
    poli_umum.enqueue("Dodi", "Nyeri perut")
    print("\n")

    #Tampilkan antrian saat ini
    poli_umum.tampilkan_antrian()
    print("\n")

    #Dokter memanggil pasien berikutnya
    poli_umum.dequeue()

    #Jumlah pasien sisa
    print(f"[INFO] Jumlah pasien masih menunggu: {poli_umum.size()} orang")
    print("\n")

    #Clear antrian (kosongkan)
    poli_umum.clear()

    #Cek apakah antrian sudah kosong
    status = "YA, antrian sudah kosong." if poli_umum.is_empty() else "TIDAK, masih ada pasien."
    print(f"[CEK] Apakah antrian kosong? → {status}")
    
    print("\n======================================")
    print("         Simulasi Selesai!          ")
    print("======================================")