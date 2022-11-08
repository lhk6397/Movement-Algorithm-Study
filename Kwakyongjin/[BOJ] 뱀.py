import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[-1 for _ in range(n+2)]]
for _ in range(n):
    graph.append([-1] + [0 for _ in range(n)] + [-1])
graph.append([-1] * (n+2))
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] += 1
l = int(input())
queue = []
for _ in range(l):
    tmp = input().rstrip().split()
    x = int(tmp[0])
    c = tmp[1]
    queue.append([x, c])
queue = deque(queue)
current_x, current_y = 1, 1
current_dir = 1
current_snake = [[1, 1]]
current_snake = deque(current_snake)
snake_back = [1, 1]
snake_back = deque(snake_back)
graph[1][1] = -1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
now_time = 0
chck = True

while queue:
    x, c = queue.popleft()
    x -= now_time


    for i in range(x):
        cnt += 1
        
        current_x += dx[current_dir]
        current_y += dy[current_dir]

        if graph[current_x][current_y] == -1:
            chck = False
            break
        
        if graph[current_x][current_y] == 1:
            graph[current_x][current_y] = -1
            current_snake.append([current_x, current_y])
        
        else:
            graph[snake_back.popleft()][snake_back.popleft()] = 0
            graph[current_x][current_y] = -1
            current_snake.append([current_x, current_y])
            current_snake.popleft()
            snake_back.append(current_snake[0][0])
            snake_back.append(current_snake[0][1])

    now_time += x
    
    if c == 'D':
        current_dir += 1
        current_dir %= 4

    if c == 'L':
        current_dir -= 1
        if current_dir == -1:
            current_dir = 3

    if chck == False:
        break

while chck:
    cnt += 1
        
    current_x += dx[current_dir]
    current_y += dy[current_dir]

    if graph[current_x][current_y] == -1:
        chck = False
        break
        
    if graph[current_x][current_y] == 1:
        graph[current_x][current_y] = -1
        current_snake.append([current_x, current_y])
        
    else:
        graph[snake_back.popleft()][snake_back.popleft()] = 0
        graph[current_x][current_y] = -1
        current_snake.append([current_x, current_y])
        current_snake.popleft()
        snake_back.append(current_snake[0][0])
        snake_back.append(current_snake[0][1])

print(cnt)
