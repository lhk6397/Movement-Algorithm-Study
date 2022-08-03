n = int(input())
nodes = [tuple(map(int, input().split())) for _ in range(n)]
arr = sorted(nodes, key=lambda x : (x[0], x[1]))
for x, y in arr:
  print(x, y)