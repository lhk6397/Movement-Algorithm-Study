# https://www.acmicpc.net/problem/11286
import sys
import heapq
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(data)[1])
        except:
            print(0)
    else:
        heapq.heappush(data, (abs(x), x))

