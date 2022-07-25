# https://www.acmicpc.net/problem/1927
import sys
import heapq
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if data:
            print(heapq.heappop(data))
        else:
            print(0)
    else:
        heapq.heappush(data, x)

