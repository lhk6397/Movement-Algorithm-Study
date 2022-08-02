n, m = map(int, input().split())
cnt = 1
while(m > n):
  if m == n:
    break
  if m // 2 >= n and m % 2 == 0:
    cnt += 1
    m //= 2
  elif (m - 1) // 10  >= n and (m - 1) % 10 == 0:
    cnt += 1
    m = (m-1) // 10
  else:
    cnt = -1
    break
print(cnt)