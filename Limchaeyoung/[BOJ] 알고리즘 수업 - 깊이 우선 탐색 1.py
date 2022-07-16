# https://www.acmicpc.net/problem/24479
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    for g in graph[v]:
        if not visited[g]:
            cnt += 1
            dfs(graph, g, visited)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for x in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()
cnt = 1
visited = [0]*(n+1)
dfs(graph, start, visited)

for x in range(1, n+1):
    print(visited[x])