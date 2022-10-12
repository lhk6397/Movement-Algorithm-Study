import sys
input = sys.stdin.readline

def dfs(x, y):
    if y == c - 1:
        return True
    
    for dx in [-1, 0, 1]:
        nx = x + dx
        ny = y + 1

        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != 'x' and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    
    return False

r, c = map(int, input().split())
visited = [[-1 for _ in range(c)] for _ in range(r)]
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))

cnt = 0
for i in range(r):
    if dfs(i, 0):
        cnt += 1

print(cnt)
