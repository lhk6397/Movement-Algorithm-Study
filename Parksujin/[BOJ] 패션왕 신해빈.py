# (종류1 + 1) * (종류2 + 1) ... -1
T = int(input())
for i in range(T):
  clo = {}
  n = int(input())
  for j in range(n):
    n, y = input().split()
    if y in clo:
      clo[y] += 1
    else:
      clo[y] = 1

  ans = 1      
  for k in clo.keys():
    ans = ans * (clo[k] + 1)
  
  print(ans-1)
  