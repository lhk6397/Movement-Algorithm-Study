# https://www.acmicpc.net/problem/10026
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, visited):
    queue = deque([(x, y, graph[x][y])])
    visited[x][y] = True
    while queue:
        x, y, color = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == color and visited[nx][ny] == False:
                queue.append((nx, ny, graph[nx][ny]))
                visited[nx][ny] = True

cnt1 = 0
cnt2 = 0
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited1 = [[False]*n for _ in range(n)]
visited2 = [[False]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if visited1[x][y] == False:
            bfs(x, y, visited1)
            cnt1 += 1

for x in range(n):
    for y in range(n):
        if graph[x][y] == 'G':
            graph[x][y] = 'R'
for x in range(n):
    for y in range(n):
        if visited2[x][y] == False:
            bfs(x, y, visited2)
            cnt2 += 1
print(cnt1, cnt2)