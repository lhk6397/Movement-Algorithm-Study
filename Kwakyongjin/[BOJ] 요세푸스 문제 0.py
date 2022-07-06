from collections import deque

n, k = map(int, input().split())
queue = [i for i in range(1, n+1)]
queue = deque(queue)
result = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print('<', end='')
print(*result, sep=', ', end='')
print('>')
