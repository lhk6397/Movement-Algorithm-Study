N = int(input())
inf = []
rank = []
for i in range(N):
  x, y = map(int, input().split())
  inf.append((x, y))

for j in range(N):
  cnt = 1
  for k in range(N):
    if inf[j][0] < inf[k][0] and inf[j][1] < inf[k][1]:
      cnt += 1
  rank.append(cnt)
  
for _ in rank:
  print(_, end = " ")
      
        
     


