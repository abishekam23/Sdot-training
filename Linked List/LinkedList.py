class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addNode(self, data):
        newnode=Node(data)
        if self.head is None:
            self.head = self.tail = newnode
            return
        self.tail.next = newnode
        self.tail = newnode

def printList(n):
    while n is not None:
        print(n.data, end="->")
        n = n.next
    print("NULL")