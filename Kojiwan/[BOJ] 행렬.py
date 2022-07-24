def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
          A[i][j] = 1 - A[i][j]

N, M = map(int, input().split())

A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

count = 0

for i in range(N-2):
  for j in range(M-2):
    if A[i][j] != B[i][j]:
      flip(i, j)
      count += 1

if A == B:
  print(count)
else:
  print("-1")