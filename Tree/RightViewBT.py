from queue import Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def right_view(root):
        if not root:
            return

        q = Queue()
        q.put(root)

        while not q.empty():
            n = q.qsize()
            for i in range(n):
                curr = q.get()
                if i == n - 1:
                    print(curr.data, end=" ")
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
if __name__ == "__main__":
    val = input().split()
    q = Queue()
    root = Node(int(val[0]))
    q.put(root)
    i=1
    while not q.empty() and (i!=len(val)):
      curr = q.get()
      l = val[i]
      if(l!="N"):
        curr.left = Node(int(l))
        q.put(curr.left)
      i+=1
      if(i<len(val)):
        r = val[i]
        if(r!="N"):
          curr.right = Node(int(r))
          q.put(curr.right)
        i+=1

    right_view(root)