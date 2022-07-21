n = int(input())

def hanoi(st, ed, n):
  if n <= 0:
    return
  hanoi(st, 6-(ed+st), n-1)
  print(st, ed)
  hanoi(6-(ed+st), ed, n-1)
  
print(2**n - 1)
if n <= 20:
  hanoi(1, 3, n)