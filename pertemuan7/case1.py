#1 Case: Sebuah sistem parkir mencatat plat nomor kendaraan yang masuk dalam sebuah array.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def MenerimaArray(head):
  for plat in head :
    print(plat)

def PlatGenap(head):
  for i in range (len(head)):
    if int(head[5]) % 2 == 0:
      head.next = head.next.exy

    currentNode = head
    while currentNode :
      if int(currentNode[5]) % 2 == 0:
        head.next = head.next.next
        currentNode = currentNode.next
    
    if currentNode.next is None:
      return head
    
    currentNode.next = currentNode.next.next
    return head

Plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
MenerimaArray(Plat)
newArray = PlatGenap(Plat)
print(newArray)