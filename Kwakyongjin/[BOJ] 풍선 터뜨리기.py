from collections import deque
import sys

n = int(input())
balloon = list(map(int, sys.stdin.readline().split()))
index = [i for i in range(1, n+1)]
total = deque()

for i in range(n):
    total.append((balloon[i], index[i]))

answer = []

data = total.popleft()
k = data[0]
answer.append(data[1])

while n-1:
    if k > 0:
        for i in range(k-1):
            total.append(total.popleft())

        data = total.popleft()
        k = data[0]
        answer.append(data[1])

    else:
        for i in range(abs(k)-1):
            total.appendleft(total.pop())

        data = total.pop()
        k = data[0]
        answer.append(data[1])
    
    n -= 1
    
print(*answer)
