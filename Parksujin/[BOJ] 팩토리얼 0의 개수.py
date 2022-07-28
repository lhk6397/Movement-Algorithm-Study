def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)
  
N = int(input())
num = factorial(N)
li = str(num)[::-1]
cnt = 0
for i in li:
  if i != '0':
   break
  cnt += 1
  
print(cnt)