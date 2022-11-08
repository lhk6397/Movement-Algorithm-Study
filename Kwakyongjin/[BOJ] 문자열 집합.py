import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = set()

for i in range(n):
    tmp = input().rstrip()
    graph.add(tmp)

cnt = 0

for i in range(m):
    tmp = input().rstrip()
    if tmp in graph:
        cnt += 1

print(cnt)
