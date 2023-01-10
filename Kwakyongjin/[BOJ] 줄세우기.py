import sys
input = sys.stdin.readline

n = int(input())
graph = [int(input().rstrip()) for _ in range(n)]
d = [0] * (n+1)
d[1] = 1

for i in range(n):
    s = []
    for j in range(i):
        if graph[i] > graph[j]:
            s.append(d[j])
    
    if not s:
        d[i] = 1
    else:
        d[i] = max(s) + 1
    
print(n - max(d))
