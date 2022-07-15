import sys
from collections import deque
input = sys.stdin.readline
def bfs(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for g in graph[v]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True
                cnt+=1
n = int(input())
m = int(input())
cnt = 0
graph = {}
for x in range(n):
    graph[x+1] = set()
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
visited = [False]*(n+1)
bfs(graph, 1, visited)
print(cnt)