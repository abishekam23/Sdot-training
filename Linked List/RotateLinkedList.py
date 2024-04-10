class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
lastNode = None

def push(data):
    global head, lastNode
    if lastNode is None:
        head = Node(data)
        lastNode = head
    else:
        lastNode.next = Node(data)
        lastNode = lastNode.next

def printList():
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def rotate(k):
    global head
    if k == 0:
        return
    current = head
    count = 1
    while count < k and current is not None:
        current = current.next
        count += 1
    if current is None:
        return
    kthNode = current
    while current.next is not None:
        current = current.next
    current.next = head
    head = kthNode.next
    kthNode.next = None

if __name__ == "__main__":
    while True:
        num = int(input())
        if num == -1:
            break
        else:
            push(num)

    print("Given linked list:")
    printList()
    rotated = int(input())
    rotate(rotated)

    print("Rotated Linked list:")
    printList()