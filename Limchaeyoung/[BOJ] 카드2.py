# https://www.acmicpc.net/problem/2164
from collections import deque
n = int(input())
deque = deque(x for x in range(1,n+1))
while len(deque) != 1:
    deque.popleft()
    deque.append(deque.popleft())
print(deque.pop())