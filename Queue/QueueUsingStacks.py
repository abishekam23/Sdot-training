s = []
n =  int(input())
for i in range(n):
  val = int(input())
  s.append(val)
k = int(input())
s2 = []
for j in range(n):
  s2.append(s.pop())
for i in range(k):
  s2.pop()

print("Queue elements are:")
while s2:
  print(s2.pop(),end = " ")