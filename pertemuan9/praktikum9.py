# Bagian A — Double Linked List

class Node :
    def __init__(self,judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul):
            new_node = Node(judul,None)

            # Jika linked list kosong
            if self.head is None:
                self.head = new_node
                return

            # Cari node terakhir
            current = self.head
            while current.next:
                current = current.next

            # Hubungkan node terakhir dengan node baru
            current.next = new_node
            new_node.prev = current
    
    # Buat fungsi print_forward() dan print_backward(), lalu jalankan keduanya.
    def display_forward(self):
        current = self.head
        while current:
            print(current.judul, end=" <-> ")
            current = current.next
        print("None")

    # Menampilkan dari belakang ke depan
    def display_backward(self):
        current = self.head

        # Pergi ke node terakhir
        while current and current.next:
            current = current.next

        # Tampilkan mundur
        while current:
            print(current.judul, end=" <-> ")
            current = current.prev
        print("None")
    
    # Menghapus node berdasarkan 
    def delete(self, judul):
        current = self.judul

        while current:
            if current.judul == judul:
                # Jika node pertama
                if current.prev is None:
                    self.judul = current.next
                    if self.judul:
                        self.judul.prev = None
                else:
                  # Menghubungkan node sebelumnya dengan node berikutnya
                    current.prev.next = current.next

                    if current.next:
                      # Menghubungkan node berikutnya dengan node sebelumnya
                        current.next.prev = current.prev
                return

            current = current.next

buku = DoublyLinkedList()

buku.insert_tail('Laskar Pelangi')
buku.insert_tail('Bumi Manusia')
buku.insert_tail('Sang Pemimpi')


buku.display_backward()
buku.display_forward()

# Bagian B — Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di akhir
    def insert_list(self, data):
        new_node = Node(data)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Sambungkan node terakhir ke node baru
        current.next = new_node
        new_node.next = self.head

    # Menambah node di awal
    def prepend(self, data):
        new_node = Node(data)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Node baru menunjuk ke head lama
        new_node.next = self.head

        # Node terakhir menunjuk ke head baru
        current.next = new_node

        # Pindahkan head
        self.head = new_node
    
    # Menghapus node berdasarkan data
    def delete_head(self, data):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            # Jika node ditemukan
            if current.data == data:
                
                # Jika hanya ada 1 node
                if current == self.head and current.next == self.head:
                    self.head = None
                    
                # Jika menghapus head
                elif current == self.head:
                    last = self.head
                    
                    # Cari node terakhir
                    while last.next != self.head:
                        last = last.next
                        
                    # Head pindah ke node berikutnya
                    self.head = self.head.next
                    
                    # Node terakhir menunjuk ke head baru
                    last.next = self.head
                    
                # Jika menghapus node biasa / terakhir
                else:
                    
                  # 10 (prev) -> 20 (current) -> 30 (current.next)
                    prev.next = current.next

                return

            # Geser ke node berikutnya (prev = None, current = 10) -> (prev = 10, current = 20) -> (prev = 20, current = 30)
            prev = current
            current = current.next

            # Jika sudah kembali ke head, berarti data tidak ada
            if current == self.head:
                break

    # Menampilkan linked list
    def display(self):
        if self.head is None:
            print("Linked list kosong")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(Kembali ke head)")
    
pelanggan = CircularLinkedList()
pelanggan.insert_list('Andi')
pelanggan.insert_list('Budi')
pelanggan.insert_list('Dina')

pelanggan.insert_list('Edo')
pelanggan.display()

pelanggan.delete_head('Andi')

pelanggan.display()