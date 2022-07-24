import copy

def dfs1(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 'R':
        stack = [(x, y)]
        graph[x][y] = 0
        
        while stack:
            x, y = stack.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue

                if graph[nx][ny] == 'G' or graph[nx][ny] == 'B':
                    continue

                if graph[nx][ny] == 'R':
                    graph[nx][ny] = 0
                    stack.append((nx, ny))
            
        return True
    
    if graph[x][y] == 'G':
        stack = [(x, y)]
        graph[x][y] = 0
        
        while stack:
            x, y = stack.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue

                if graph[nx][ny] == 'R' or graph[nx][ny] == 'B':
                    continue

                if graph[nx][ny] == 'G':
                    graph[nx][ny] = 0
                    stack.append((nx, ny))
            
        return True

    if graph[x][y] == 'B':
        stack = [(x, y)]
        graph[x][y] = 0
        
        while stack:
            x, y = stack.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue

                if graph[nx][ny] == 'G' or graph[nx][ny] == 'R':
                    continue

                if graph[nx][ny] == 'B':
                    graph[nx][ny] = 0
                    stack.append((nx, ny))
            
        return True
    
    return False

def dfs2(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph2[x][y] == 'R' or graph2[x][y] == 'G':
        stack = [(x, y)]
        graph2[x][y] = 0
        
        while stack:
            x, y = stack.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue

                if graph2[nx][ny] == 'B':
                    continue

                if graph2[nx][ny] == 'R' or graph2[nx][ny] == 'G':
                    graph2[nx][ny] = 0
                    stack.append((nx, ny))
            
        return True
    
    if graph2[x][y] == 'B':
        stack = [(x, y)]
        graph2[x][y] = 0
        
        while stack:
            x, y = stack.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue

                if graph2[nx][ny] == 'R' or graph2[nx][ny] == 'G':
                    continue

                if graph2[nx][ny] == 'B':
                    graph2[nx][ny] = 0
                    stack.append((nx, ny))
        return True

    return False


n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))

graph2 = copy.deepcopy(graph)

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result1 = 0
for i in range(n):
    for j in range(n):
        if dfs1(i, j) == True:
            result1 += 1

result2 = 0
for i in range(n):
    for j in range(n):
        if dfs2(i, j) == True:
            result2 += 1

print(result1, result2)
