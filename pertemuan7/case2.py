class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def tambahKendaraan(plat, newNode, position):
   currentNode = plat
   for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next
    newNode.next = currentNode.next
    currentNode.next = newNode
    return plat


def hapusKendaraan(plat):
   currentNode = plat
   for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next
    newNode.next = currentNode.next
    currentNode.next = newNode
    return plat
  
node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4
  
print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node()
node1 = tambahKendaraan(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)
