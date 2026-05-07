class Node:
    """Representasi Node dalam Binary Search Tree"""
    def __init__(self, id_buku, judul):
        self.id_buku = int(id_buku)
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    """Implementasi Binary Search Tree"""
    def __init__(self):
        self.root = None
        self.nomor = 1
    
    #Menambahkan buku baru ke dalam BST sesuai aturan ID (Kiri < Parent < Kanan).
    def insert(self, id_buku, judul):
        node_new = Node(id_buku, judul)
        if self.root is None:
            self.root = node_new
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        
        P = self.root
        Q = self.root
        
        while Q is not None and node_new.id_buku != P.id_buku:
            P = Q
            if node_new.id_buku < P.id_buku:
                Q = P.left
            else:
                Q = P.right

        if P.id_buku > node_new.id_buku:
            P.left = node_new
        else:
            P.right = node_new
        
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
    
    #Mencari apakah suatu buku ada di katalog berdasarkan ID-nya.
    def search(self, id_buku):
        print(f"\n[SEARCH] Mencari ID {id_buku} ... ", end="")
        curr = self.root
        find = False
        while curr is not None:
            if curr.id_buku > id_buku:
                curr = curr.left
            elif curr.id_buku < id_buku:
                curr = curr.right
            else:
                find = curr.judul
                break
        if find:
            print(f"Ditemukan! Judul: {find}")
        else:
            print("Data tidak ditemukan.")
    
    #Menampilkan semua koleksi buku secara urut dari ID terkecil ke terbesar.
    def traversal_inorder(self, node):
        if node is not None:
            self.traversal_inorder(node.left)
            print(f"{self.nomor}. {node.id_buku} - {node.judul}")
            self.nomor += 1
            self.traversal_inorder(node.right)
    
    #Menemukan buku dengan ID terkecil.
    def get_min(self):
        if self.root is None:
            return None
        min = self.root
        while min.left is not None:
            min = min.left
        return min.id_buku
    
    #Menemukan buku dengan ID terbesar.
    def get_max(self):
        if self.root is None:
            return None
        max = self.root
        while max.right is not None:
            max = max.right
        return max.id_buku
    
    #Menghitung total ketinggian (height) dari tree yang terbentuk.
    def height(self, node):
        if node is None:
            return -1 
        
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        
        return max(left_h, right_h) + 1
    
#Main program
bst = BinarySearchTree()

print("\n=========================================")
print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=========================================")

#1. Input Data
bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

#2. Cek Koleksi
print("\n[INFO] Koleksi Buku (In-Order Traversal):")
bst.traversal_inorder(bst.root)

#3. Pencarian
bst.search(60)
bst.search(100)

#4. Statistik & Analisis Struktur
print(f"\n[STATISTIK] ID Terkecil: {bst.get_min()}")
print(f"[STATISTIK] ID Terbesar: {bst.get_max()}")
print(f"[INFO] Tinggi (Height) Tree: {bst.height(bst.root)}")
print("=========================================")
print("Simulasi Selesai!")
print("=========================================")