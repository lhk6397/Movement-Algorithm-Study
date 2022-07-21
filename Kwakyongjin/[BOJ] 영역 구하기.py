import sys

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return 0, 0
    
    if graph[x][y] == 1:
        return 0, 0
    
    if graph[x][y] == 0:
        visited = []
        stack = [(x, y)]
        count = 1

        while stack:
            x, y = stack.pop()
            visited.append((x, y))
            graph[x][y] = 2
            
            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                    continue
    
                if graph[nx][ny] == 1:
                    continue

                if graph[nx][ny] == 0 and not (nx, ny) in visited:
                    stack.append((nx, ny))
                    visited.append((nx, ny))
                    graph[nx][ny] = 2
                    count += 1
        return 1, count
    return 0, 0
                

m, n, k = map(int, input().split())
graph = [[0 for i in range(n)] for i in range(m)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(abs(x1 - x2)):
        for j in range(abs(y1 - y2)):
            graph[y1+j][x1+i] = 1

total = 0
width = []
for i in range(m):
    for j in range(n):
        result, count2 = dfs(i, j)
        if result == 1:
            total += result
            width.append(count2)
print(total)
width.sort()
print(*width)
