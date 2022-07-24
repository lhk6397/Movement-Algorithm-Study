import sys
from collections import deque

def bfs1(x, y):
    global a
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    graph[x][y] = a

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = a
                queue.append((nx, ny))

def bfs2(theta):
    global answer
    global n
    bridge_length = [[-1] * n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == theta:
                queue.append((i, j))
                bridge_length[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] > 0 and graph[nx][ny] != theta:
                answer = min(answer, bridge_length[x][y])
                return

            if graph[nx][ny] == 0 and bridge_length[nx][ny] == -1:
                bridge_length[nx][ny] = bridge_length[x][y] + 1
                queue.append((nx, ny))

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

a = 1
answer = 10001
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs1(i, j)
            a += 1

for i in range(1, a):
    bfs2(i)

print(answer)
