from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
cnt = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for st in range(1, n + 1):
  if visited[st] == True:
    continue
  q = deque([st])
  visited[st] = True
  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
  cnt += 1

print(cnt)