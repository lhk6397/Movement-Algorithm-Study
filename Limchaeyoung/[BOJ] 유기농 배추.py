# https://www.acmicpc.net/problem/1012
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(graph, x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for x in range(m):
        for y in range(n):
            if graph[x][y] == 1:
                bfs(graph, x, y)
                cnt += 1
    print(cnt)