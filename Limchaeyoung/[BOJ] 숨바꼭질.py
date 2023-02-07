# https://www.acmicpc.net/problem/1697
from collections import deque

n, k = map(int, input().split())
sec = [-1] * 100001
s = [-1,1,2]

def bfs(n):
    queue = deque([n])
    sec[n] = 0
    while queue:
        q = queue.popleft()
        for i in s:
            x = q * 2 if i == 2 else q + i
            if 0 <= x <= 100000 and sec[x] == -1:
                queue.append(x)
                sec[x] = sec[q] + 1
            if x == k:
                 return sec[x]

print(bfs(n))