n = int(input())
stack = [] # 순서대로 push [12345]
res = [] # pop [+++--++]
cnt = 1
tmp = True

for i in range(n):
  num = int(input())
  while num >= cnt: 
    stack.append(cnt)
    res.append('+')
    cnt += 1
    
  if stack[-1] == num: # stack의 top이 예제의 숫자와 같다면
    stack.pop()
    res.append('-')
  else: 
    tmp = False
  
if tmp == False:
  print('NO')
else:
  for j in res:
    print(j)
    
    
  