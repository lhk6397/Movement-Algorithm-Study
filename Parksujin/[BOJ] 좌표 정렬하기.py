N = int(input())
# list_x = []
# list_y = []
# for i in range(N):
#   x, y = map(int, input().split())
#   list_x.append(x)
#   list_y.append(y)
  
# list_x.sort()
# list_y.sort()

# for j in range(N):
#   print(list_x[j], list_y[j])

list = []
for i in range(N):
  x, y = map(int, input().split())
  list.append((x,y))

list.sort()

for j in range(N):
  print(list[j][0], list[j][1])