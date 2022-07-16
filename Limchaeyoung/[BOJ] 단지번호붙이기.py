# https://www.acmicpc.net/problem/2667
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(graph, x, y):
    queue = deque([(x, y)])
    cnt = 1
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
    cnt_list.append(cnt)
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cnt_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(graph, i, j)
cnt_list.sort()
print(len(cnt_list))
for i in range(len(cnt_list)):
    print(cnt_list[i])

'''
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(graph, x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph, nx, ny)
        return True

cnt = 0
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cnt_list = []
for i in range(n):
    for j in range(n):
        if dfs(graph, i, j) == True:
            cnt_list.append(cnt)
            cnt = 0
cnt_list.sort()
print(len(cnt_list))
for i in range(len(cnt_list)):
    print(cnt_list[i])
'''