from collections import deque
import sys

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1
 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


    
n, m = map(int,input().split())
graph = []
total = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            total.append(bfs(graph, i, j))
    

if len(total) == 0:
    print(len(total))
    print(0)

else:
    print(len(total))
    print(max(total))
