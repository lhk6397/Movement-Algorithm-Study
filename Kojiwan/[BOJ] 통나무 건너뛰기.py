import sys

T = int(input())
for _ in range(T):
  n = int(input())
  arr = list(map(int, sys.stdin.readline().split()))
  arr.sort()
  first_gap = arr[1] - arr[0]
  last_gap = arr[-1] - arr[-2]
  max_gap = max(first_gap, last_gap)
  for st in range(len(arr) - 2):
    gap = abs(arr[st+2] - arr[st])
    max_gap = max(max_gap, gap)
    
  print(max_gap)
  