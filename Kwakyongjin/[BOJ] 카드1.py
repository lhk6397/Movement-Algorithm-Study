from collections import deque

queue = deque()
result = []
n = int(input())
for i in range(1, n+1):
    queue.append(i)
    
while queue:
    result.append(queue.popleft())
    if queue:
        queue.append(queue.popleft())
    else:
        break

for i in result:
    print(i, end=' ')
