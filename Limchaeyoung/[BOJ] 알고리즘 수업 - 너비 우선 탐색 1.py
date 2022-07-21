# https://www.acmicpc.net/problem/24444
import sys
from collections import deque
input = sys.stdin.readline
def bfs(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = cnt
    while queue:
        v = queue.popleft()
        for g in graph[v]:
            if not visited[g]:
                queue.append(g)
                cnt += 1
                visited[g] = cnt

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()
cnt = 1
visited = [0]*(n+1)
bfs(graph, start, visited)

for x in range(1, n+1):
    print(visited[x])