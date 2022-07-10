import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    # 동, 서, 남, 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(0, 0))
