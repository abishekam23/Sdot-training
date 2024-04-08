class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
    def addNode(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
            return
        self.tail.next = newnode
        self.tail = newnode

def printList(n):
    while n is not None:
        print(n.data, end=" ")
        n = n.next
    print()        

def OddEvenList(head):
    if head is None or head.next is None:
        return head
    oddlst = head
    evenlst = head.next
    evenhead = evenlst
    while evenlst is not None and evenlst.next is not None and oddlst.next is not None:
        oddlst.next = evenlst.next
        oddlst = oddlst.next
        evenlst.next = oddlst.next
        evenlst = evenlst.next
    oddlst.next = evenhead
    return head


if __name__=="__main__":
    n=int(input())
    lst1 = LinkedList()
    data = input().split(" ")
    for i in range(n):
        lst1.addNode(data[i])
    output = OddEvenList(lst1.head)
    printList(output)