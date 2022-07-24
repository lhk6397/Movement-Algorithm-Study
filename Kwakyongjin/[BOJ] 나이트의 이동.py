from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            if not graph[end_x][end_y] == 0:
                print(graph[end_x][end_y] - 1)
                return
            else:
                print(graph[end_x][end_y])
                return

        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
            

t = int(input())
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for _ in range(t):
    n = int(input())
    graph = [[0 for i in range(n)] for j in range(n)]
    start_x, start_y = map(int,input().split())
    graph[start_x][start_y] = 1
    queue = deque()
    queue.append((start_x, start_y))
    end_x, end_y = map(int,input().split())
    graph[end_x][end_y] = 0
    bfs()
