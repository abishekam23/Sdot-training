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

def printList(n):
    while n is not None:
        print(n.data, end="->")
        n = n.next
    print("NULL")

if __name__ == "__main__":
   n = int(input())
   lst1=LinkedList()
   data1= input().split(" ")
   data1=data1[:-1]
   size1 = len(data1)
   for j in range(size1):
        lst1.addNode(int(data1[j])) 
   if n > 1:
        for i in range(n-1):
            lst2 = LinkedList()
            data2 = input().split(" ")[:-1]
            size2 = len(data2)
            for k in range(size2):
                lst2.addNode(int(data2[k]))
            header = lst1.head
            lst = mergesortlist(header,lst2.head)
            lst1 = lst
        printList(lst1.head)
   else:
       printList(lst1.head)
 



        
      

      