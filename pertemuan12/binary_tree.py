class Node:
    """Representasi Node dalam Binary Tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Insert Manual
class BinaryTree:
    """Implementasi Binary Tree"""
    def __init__(self):
        self.root = None
    
    def insert_root(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        """Memasukkan child kiri dari Node"""
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        """Memasukkan child kanan dari Node"""
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

bt = BinaryTree()

"""Skenario Pengujian"""
bt.insert_root("A")
bt.insert_left(bt.root, "B")
bt.insert_right(bt.root, "C")
bt.insert_left(bt.root.left, "D")
bt.insert_right(bt.root.left, "E")
bt.insert_right(bt.root.right, "F")

#1. Audit Prioritas (Pre-Order): Mengecek gudang utama sebelum cabang-cabangnya.
def traverse_preorder(node):
    """"Pre-Order: Root -> Kiri -> Kanan"""
    if node is not None:
        print(node.data, end=" - ")
        traverse_preorder(node.left)
        traverse_preorder(node.right)

#2. Audit Berurutan (In-Order): Mengecek dari jalur kiri, lalu pusat, baru ke kanan.
def traverse_inorder(node):
    """"In-Order: Kiri -> Root -> Kanan"""
    if node is not None:
        traverse_inorder(node.left)
        print(node.data, end=" - ")
        traverse_inorder(node.right)

#3. Audit Akhir (Post-Order): Mengecek semua cabang terlebih dahulu sebelum kembali ke gudang pusat.
def traverse_postorder(node):
    """"Post-Order: Kiri -> Kanan -> Root"""
    if node is not None:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(node.data, end=" - ")

#Tampilan Output
#4. Menampilkan daftar gudang yang merupakan Leaf Node (gudang ujung yang tidak punya cabang lagi).
def get_leaf_nodes(node):
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [node.data]
    
    #Rekursif ke kiri dan ke kanan
    return get_leaf_nodes(node.left) + get_leaf_nodes(node.right)
    pass

#Main Program
print("\n======================================")
print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.")

print("\n")
print("HASIL AUDIT:")
print("\n1. Pre-Order  : ", end="")
traverse_preorder(bt.root)
print("\n2. In-Order   : ", end="")
traverse_inorder(bt.root)
print("\n3. Post-Order : ", end="")
traverse_postorder(bt.root)

print("\n")
print(f"[DATA] Gudang Ujung (Leaf Nodes): {", " .join (get_leaf_nodes(bt.root))}")
print("======================================")
print("Audit Selesai!")
print("======================================")