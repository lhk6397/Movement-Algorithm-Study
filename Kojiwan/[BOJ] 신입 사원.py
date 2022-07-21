import sys

T = int(input())
for _ in range(T):
  result = 1
  data = []
  n = int(sys.stdin.readline())
  for i in range(n):
    data.append(tuple(map(int, sys.stdin.readline().split())))
  
  data.sort()
  target = data[0][1]
 
  for k in range(1,n):
    if target > data[k][1]:
      result+=1
      target = data[k][1]
  
  print(result)