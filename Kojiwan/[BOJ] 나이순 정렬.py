n = int(input())
nodes = [list(input().split()) for _ in range(n)]
for i in range(len(nodes)):
  nodes[i][0] = int(nodes[i][0])
  nodes[i].append(i)
nodes.sort(key= lambda x: (x[0], x[2]))
for x, y, _ in nodes:
  print(x, y)