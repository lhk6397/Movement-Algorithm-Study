T = int(input()) # 테스트 케이스

# 목표 지점에 도달하는 경우의 수는 3가지 밖에 없음 -> 목표 지점의 관점에서 보자
while T:
  row, col = map(int, input().split())
  arr = list(map(int, input().split()))

  d = []
  i = 0
  for _ in range(row):
    d.append(arr[i: i + col])
    i += col
    
  for j in range(1, col):
    for i in range(row):
      target = d[i][j]
      d[i][j] += d[i][j-1]
      if i-1 >= 0:
        d[i][j] = max(d[i][j], target + d[i-1][j-1])
      if i+1 < row:
        d[i][j] = max(d[i][j], target + d[i+1][j-1])
  
  max_gold = 0
  for i in range(row):
    max_gold = max(max_gold, d[i][col-1])
    
  print(max_gold)
  T -= 1