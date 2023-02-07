# https://www.acmicpc.net/status?user_id=hea_c&problem_id=13549&from_mine=1
from collections import deque

n, k = map(int, input().split())
sec = [-1] * 100001
s = [2, -1, 1]

def bfs(n):
    queue = deque([n])
    sec[n] = 0
    while queue:
        q = queue.popleft()
        for i in s:
            if i == 2:
                tp = 1
                x = q * 2
            else:
                tp = 0
                x = q + i
            if 0 <= x <= 100000 and sec[x] == -1:
                if tp:
                    queue.append(x)
                    sec[x] = sec[q]
                else:
                    queue.append(x)
                    sec[x] = sec[q]+1
            if x == k:
                 return sec[x]

print(bfs(n))