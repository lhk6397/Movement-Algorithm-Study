from copy import deepcopy

n = int(input())
cur1_board = list(map(int, input()))
want = list(map(int, input()))
result = -1
result1 = 0
result2 = 1
cur2_board = deepcopy(cur1_board)

def flip(index, board):
  for i in range(index-1, index+2):
    if i < 0 or i >= len(board):
      continue
    board[i] = abs(board[i] - 1)

flip(0, cur2_board)
# CASE 1 (1번 전구 off)
for i in range(1, len(cur1_board)):
  if cur1_board[i-1] != want[i-1]:
    flip(i, cur1_board)
    result1 += 1
if cur1_board == want:
  result = result1
# CASE 2 (1번 전구 on)
for i in range(1, len(cur2_board)):
  if cur2_board[i-1] != want[i-1]:
    flip(i, cur2_board)
    result2 += 1
if result != -1 and cur2_board == want:
  result = min(result, result2)
elif result == - 1 and cur2_board == want:
  result = result2
  
print(result)