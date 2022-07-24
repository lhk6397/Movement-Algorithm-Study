import sys

def dfs(x, y):
    if x <= -1 or x >= w or y <= -1 or y >= h:
        return 0

    if graph[x][y] == 0:
        return 0

    if graph[x][y] == 1:
        visited = []
        stack = [(x, y)]

        while stack:
            x, y = stack.pop()
            visited.append((x, y))
            # 동, 서, 남, 북, 북동, 남동, 남서, 북서
            dx = [0, 0, 1, -1, -1, 1, 1, -1]
            dy = [1, -1, 0, 0, 1, 1, -1, -1]

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= w or ny <= -1 or ny >= h:
                    continue

                if graph[nx][ny] == 0:
                    continue

                if graph[nx][ny] == 1:
                    stack.append((nx, ny))
                    visited.append((nx, ny))
                    graph[nx][ny] = 2
        return 1

    return 0

while True:
    h, w = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(w):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    result = 0
    for i in range(w):
        for j in range(h):
            count = dfs(i, j)
            if count == 1:
                result += 1
    print(result)
