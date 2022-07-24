# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    queue = deque([(0,0)])
    visited[0][0] = 1
    maps[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if visited[nx][ny] == -1 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                maps[nx][ny] == 0
                queue.append((nx, ny))
    return visited[len(maps)-1][len(maps[0])-1]