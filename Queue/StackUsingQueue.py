from collections import deque

class Stack:
    def __init__(self) -> None:
        self.Queue1 = deque()
        self.Queue2 = deque()

    def push(self, x):
        self.Queue2.append(x)
        while self.Queue1:
            self.Queue2.append(self.Queue1.popleft())
        self.Queue1,self.Queue2 = self.Queue2,self.Queue1
    
    def pop(self):
        if not self.Queue1:
            return -1
        return self.Queue1.popleft()
    
    def top(self):
        if not self.Queue1:
            return -1
        return self.Queue1[0]
    
    def isempty(self):
        return not self.Queue1
    
if __name__ == "__main__":
    stack = Stack()
    v = int(input())
    while v != -1:
        if v == 1:
            t = int(input())
            stack.push(t)
        elif v == 2:
            print("Pop:", stack.pop())
        elif v == 3:
            print("Top element:", stack.top())
        elif v == 4:
            #print("Is empty:")
            if(stack.isempty()):
              print("Is empty: true")
            else:
              print("Is empty: false")
        v = int(input())
    
        