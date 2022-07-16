# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start, visited_dfs):
    visited_dfs.append(start)
    for i in graph[start]:
        if i not in visited_dfs:
            dfs(graph, i, visited_dfs)

def bfs(graph, start, visited):
    queue = deque([start])
    visited_bfs.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited_bfs:
                queue.append(i)
                visited_bfs.append(i)

n, m, start = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()
visited_dfs = []
visited_bfs = []
dfs(graph, start, visited_dfs)
bfs(graph, start, visited_bfs)

for x in visited_dfs:
    print(x, end=' ')
print('')
for x in visited_bfs:
    print(x, end=' ')