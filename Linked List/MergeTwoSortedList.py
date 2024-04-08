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
    
def mergesortlist(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    temp = Node(-1)
    head = temp

    while l1 is not None and l2 is not None:
      if l1.data < l2.data:
        temp.next = l1
        temp = temp.next
        l1 = l1.next
      else:
        temp.next = l2
        temp = temp.next
        l2 = l2.next
    while l2 is not None:
      temp.next = l2
      temp = temp.next
      l2 = l2.next
    while l1 is not None:
      temp.next = l1
      temp = temp.next
      l1 = l1.next
    return head.next
def printList(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("NULL")
        

if __name__=="__main__":
    size_lst1 = int(input())
    lst1 = LinkedList()
    data_lst1 = input().split(" ")
    for i in range(size_lst1):
        lst1.addNode(int(data_lst1[i]))

    size_lst2 = int(input())
    lst2 = LinkedList()
    data_lst2  = input().split(" ")
    for i in range(size_lst2):
        lst2.addNode(int(data_lst2[i]))
    merge=mergesortlist(lst1.head,lst2.head)
    printList(merge)
    