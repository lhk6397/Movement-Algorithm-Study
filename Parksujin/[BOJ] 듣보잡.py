N, M = map(int, input().split())
d= []
b= []

for i in range(N):
  a = input()
  d.append(a)
for j in range(M):
  c = input()
  b.append(c)
  
res = list(set(d) & set(b))
res.sort()

print(len(res))

for k in res:
  print(k)
