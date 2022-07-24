n = int(input())
result = 0
arr=[]
# 1. 1 ~ n-1번 원판을 2번에 옮긴다.
# 2. n번 원판을 3번에 옮긴다.
# 3. 1 ~ n-1번 원판을 3번으로 옮긴다.

def hanoi(st, ed, n):
  global result
  if n <= 0:
    return
  hanoi(st, 6-(ed+st), n-1)
  arr.append((st, ed))
  result += 1
  hanoi(6-(ed+st), ed, n-1)  
  
hanoi(1, 3, n)
print(result)
for (st, ed) in arr:
  print(st, ed)