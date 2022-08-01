from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n+1)]
cnt = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph, start, visited):
  global cnt
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    cnt += 1
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(graph, 1, visited)
print(cnt - 1)