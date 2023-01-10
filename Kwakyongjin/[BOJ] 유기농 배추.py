import sys
input = sys.stdin.readline

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return 0

    if graph[x][y] == 0:
        return 0
    
    if graph[x][y] == 1:
        visited = []
        stack = [(x, y)]

        while stack:
            x, y = stack.pop()
            visited.append((x, y))

            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                    continue

                if graph[nx][ny] == 0:
                    continue

                if graph[nx][ny] == 1:
                    stack.append((nx, ny))
                    visited.append((nx, ny))
                    graph[nx][ny] = 2
        return 1

    return 0

t = int(input().rstrip())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
        
    print(cnt)
