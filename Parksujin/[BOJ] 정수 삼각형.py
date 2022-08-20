N = int(input())
num = []
for i in range(N):
  num.append(list(map(int, input().split())))
  
for j in range(1, N): # 헹
  for k in range(j + 1): # 열
    if k == 0:
      num[j][k] = num[j][k] + num[j-1][k]
    elif k == j:
      num[j][k] = num[j][k] + num[j-1][k-1]
    else:
      num[j][k] = max(num[j][k] + num[j-1][k-1], num[j][k] + num[j-1][k])
    
print(max(num[N-1]))