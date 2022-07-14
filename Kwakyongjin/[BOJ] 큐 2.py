from collections import deque # deque를 이용하여 queue를 구현
import sys

queue = deque() # deque 생성
n = int(input())
for i in range(n):
    sentence = list(sys.stdin.readline().split()) 
    if sentence[0] == 'push':
        queue.append(sentence[1])
    elif sentence[0] == 'pop':
        if queue:
            print(queue.popleft()) # 첫번째를 pop함
        else:
            print(-1)
    elif sentence[0] == 'size':
        print(len(queue))
    elif sentence[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif sentence[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif sentence[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
