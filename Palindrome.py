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

def isPalindrome(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    prev = slow
    slow = slow.next
    prev.next = None
    while slow is not None:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    fast = head
    slow = prev
    while slow is not None:
        if fast.data != slow.data:
            return False
        fast = fast.next
        slow = slow.next
    return True

if __name__ == "__main__":
    head = None
    n = int(input())
    lst1 = LinkedList()
    data = input().split(" ")
    for i in range(n):
        lst1.addNode(int(data[i]))
    print(isPalindrome(lst1.head))


