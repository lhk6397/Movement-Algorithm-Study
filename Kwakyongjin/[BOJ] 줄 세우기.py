import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
d = [0] * (n+1)

for i in range(n):
    tmp = graph[i]
    d[tmp] = d[tmp-1] + 1
print(n-max(d))
