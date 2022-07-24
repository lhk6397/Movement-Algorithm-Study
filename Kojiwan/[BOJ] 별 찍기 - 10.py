n = int(input())
board = [['*'] * n for _ in range(n)]
def draw_star(i, j, n):
  global board
  check = n // 3
  if n == 1:
    return 
  if i % n in [0, check, 2 * check]:
    if (i % n == check) and (j % n == check):
      for n in range(i, i + check):
        for m in range(j, j + check):
          board[n][m] = ' '
  else:
      draw_star(i, j, check)

for i in range(n):
  for j in range(n):
    draw_star(i, j, n)
for a in board:
  for b in a:
    print(b, end="")
  print()