from collections import deque
import sys

t = int(input())
n, m = map(int, input().split())
c = int(input())
visited = [0] * (t+1)
dic={}

for i in range(t):
    dic[i+1] = set()

for j in range(c):
    a, b = map(int,input().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(n): # n을 기준으로 m 찾기
    queue = deque()
    queue.append(n)

    while queue:
        now = queue.popleft()

        for i in dic[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                queue.append(i)


bfs(n)

print(visited[m] if visited[m] > 0 else -1)
