# https://www.acmicpc.net/problem/2178
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if nx == n - 1 and ny == m - 1:
                print(graph[x][y]+1)
                return
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
bfs()