import sys
input = sys.stdin.readline
from collections import deque

n, l = map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()
queue = deque(graph)

for _ in range(n):
    current = queue.popleft()

    if l >= current:
        l += 1

    else:
        break
print(l)
