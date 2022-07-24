N = int(input())
num1 = sorted(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))

cnt = {}
for i in num1:
  if i in cnt:
    cnt[i] += 1
  else:
    cnt[i] = 1
    
for j in num2:
  if j in cnt:
    print(cnt[j], end = ' ')
  else:
    print(0, end = ' ')
  
      
