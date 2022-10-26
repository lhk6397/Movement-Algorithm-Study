import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {}
for i in range(n):
    tmp = input().split()
    graph[tmp[0]] = tmp[1]

for i in range(m):
    target = input().rstrip()
    print(graph[target])
