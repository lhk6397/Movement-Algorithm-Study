# https://www.acmicpc.net/problem/1463
n = int(input())

d = [0] * (n + 1)

d[1] = 0

for i in range(2, n + 1):
  temp1, temp2, temp3 = n, n, n
  if i % 5 == 0:
    temp1 = d[i // 5] + 1
  if i % 3 == 0:
    temp2 = d[i // 3] + 1
  if i % 2 == 0:
    temp3 = d[i // 2] + 1
  d[i] = min(d[i - 1] + 1, temp1, temp2, temp3)
print(d[n])