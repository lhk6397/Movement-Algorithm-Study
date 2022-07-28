from collections import deque
from itertools import combinations

def bfs(board, Q, visited):
  cnt = 0
  while Q:
    x, y = Q.popleft()
    for dir in range(4):
      nx = x + dx[dir]
      ny = y + dy[dir]
      if 0 <= nx < n and 0 <= ny < m:
        if board[nx][ny] == 0 and visited[nx][ny] == False:
          Q.append((nx, ny))
          visited[nx][ny] = True
          cnt += 1
  return cnt

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]* m for _ in range(n)]
virus = []
result = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# 바이러스 위치 찾기
for i in range(n):
  for j in range(m):
    if board[i][j] == 2:
      virus.append((i, j))
      visited[i][j] = True

data = []
for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      data.append((i, j))
combi = list(combinations(data, 3))

for pairs_3 in combi:
  temp_visited = [[0]* m for _ in range(n)]
  # 벽 세우기
  for x, y in pairs_3:
    board[x][y] = 1
  
  bfs(board, deque(virus), temp_visited)
  zero_Q = deque()
  cnt = 0
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0 and temp_visited[i][j] == 0:
        zero_Q.append((i, j))
        temp_visited[i][j] = True
        cnt += bfs(board, zero_Q, temp_visited) + 1
  
  # 벽 원상복귀
  for x, y in pairs_3:
    board[x][y] = 0
  result = max(cnt, result)
print(result)

# 모범 답안
# from itertools import combinations

# dx,dy = [0,0,1,-1],[1,-1,0,0]
# N,M = map(int,input().split())
# arr = [list(map(int,input().split())) for ARR in range(N)]
# cnt_max = 0


# def blocking(list):
#     global virus_max
#     arr_new = [i[:] for i in arr]
#     for i in list:
#         a = i//8
#         b= i%8
#         arr_new[a][b] = 1
#     virus2=virus[:] 
#     cnt = 0
#     cntt=dfs(arr_new,virus2,cnt)  
    
#     if cntt<virus_max:
#         virus_max=cntt
    
# def dfs(arr_new,vir,cnt):
#     global virus_max
#     while vir:
#         z=vir.pop()
#         node_y=z//8
#         node_x=z%8
#         if virus_max<=cnt:
#             return 64
#         for i in range(4):    
#             ny = node_y + dy[i]
#             nx = node_x + dx[i]
#             if 0<=nx<M and 0<=ny<N and arr_new[ny][nx] == 0: 
#                 vir.append(ny*8+nx)  
#                 arr_new[ny][nx] = 2  
#                 cnt+=1
        
#     return cnt

# # 벽을 세울 수 있는 후보군 찾기
# possible_block = []
# virus=[]
# safe_zone=0
# virus_max=64
# for y in range(N):
#     for x in range(M):
#         if arr[y][x] == 0:
#             possible_block.append(y*8+x)
#             safe_zone+=1
#         elif arr[y][x]==2:
#             virus.append(y*8+x)  
# block_3_list = combinations(possible_block,3)

# for i in block_3_list:
#     blocking(i)

# print(safe_zone-virus_max-3)