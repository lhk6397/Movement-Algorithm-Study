import sys
from collections import deque
input = sys.stdin.readline
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for g in graph[v]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()
visited = [False]*(n+1)
bfs(graph, 1, visited)
print(visited.count(True)-1)