# https://www.acmicpc.net/problem/1715
import sys
import heapq
input = sys.stdin.readline
n = int(input())
data = []
sum = 0
for _ in range(n):
    heapq.heappush(data, int(input()))
if n == 1:
    print(0)
else:
    while len(data) != 1:
        a = heapq.heappop(data) + heapq.heappop(data)
        sum += a
        heapq.heappush(data, a)
    print(sum)