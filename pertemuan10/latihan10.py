print("\nList Biasa Hera")
class StackList:
    def __init__(self):
        self.items = []
  
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items[-1]
  
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

StackList1 = StackList()

StackList1.push('yt.com')
StackList1.push('ig.com')
StackList1.push('tiktok.com')

print("Stack: ", StackList1.items)
print("Pop: ", StackList1.pop())
print("Stack setelah Pop: ", StackList1.items)
print("Peek: ", StackList1.peek())
print("isEmpty: ", StackList1.isEmpty())
print("Size: ", StackList1.size())

print("\nLinked List Hera")
class Node:
  def __init__(self, url):
    self.url = url
    self.next = None

class StackLinkedList:
  def __init__(self):
    self.top = None
    self.count = 0

  def push(self, url):
    new_node = Node(url)
    if self.top:
      new_node.next = self.top
    self.top = new_node
    self.count += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.top
    self.top = self.top.next
    self.count -= 1
    return popped_node.url

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.top.url

  def isEmpty(self):
    return self.count == 0

  def stackSize(self):
    return self.count

  def traverseAndPrint(self):
    currentNode = self.top
    while currentNode:
      print(currentNode.url, end=" -> ")
      currentNode = currentNode.next
    print()

StackLinked2 = StackLinkedList()

StackLinked2.push('yt.com')
StackLinked2.push('ig.com')
StackLinked2.push('tiktok.com')

print("LinkedList: ", end="")
StackLinked2.traverseAndPrint()
print("Peek: ", StackLinked2.peek())
print("Pop: ", StackLinked2.pop())
print("LinkedList setelah Pop: ", end="")
StackLinked2.traverseAndPrint()
print("isEmpty: ", StackLinked2.isEmpty())
print("Size: ", StackLinked2.stackSize())
