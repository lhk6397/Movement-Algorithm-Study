# https://www.acmicpc.net/problem/1966
T = int(input())

for _ in range(T):
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  priority = sorted(arr, reverse=True)
  for i in range(n):
    arr[i] = (arr[i], i)
  
  for i in range(n):
    while arr[i][0] < priority[i]:
      target = arr[i]
      del arr[i]
      arr.append(target)
  temp = list(x[1] for x in arr)
  print(temp.index(m) + 1)