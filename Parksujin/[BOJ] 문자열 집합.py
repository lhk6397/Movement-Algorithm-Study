N, M = map(int, input().split())
res = 0
inc = set() # 시간초과 X
for i in range(N):
  inc.add(input()) 
for j in range(M):
  test = input()
  if test in inc:
    res += 1

print(res)
  

  

