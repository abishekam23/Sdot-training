class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append(data):
    global head
    new_node = Node(data)
    temp = head
    if head is None:
        head = new_node
    else:
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    return head

def display(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next

def reverseKGroup(head, k):
    dummy = Node(0)
    dummy.next = head
    pointer = dummy
    while pointer is not None:
        node = pointer
        for i in range(k):
            if node is None:
                break
            node = node.next
        if node is None:
            break
        prev = None
        curr = pointer.next
        next_node = None
        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        tail = pointer.next
        tail.next = curr
        pointer.next = prev
        pointer = tail
    return dummy.next

if __name__ == "__main__":
    head = None
    while True:
        data = int(input())
        if data >= 0:
            head = append(data)
        else:
            break
    rev_val = int(input())
    temp = reverseKGroup(head, rev_val)
    display(temp)