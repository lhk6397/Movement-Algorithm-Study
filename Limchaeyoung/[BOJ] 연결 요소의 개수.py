# https://www.acmicpc.net/problem/11724
from collections import deque
def bfs(start):
    queue = deque([start])
    visited.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

n, m = map(int, input().split())
cnt = 0
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = []
for i in range(1, n+1):
    if i not in visited:
        bfs(i)
        cnt += 1
print(cnt)