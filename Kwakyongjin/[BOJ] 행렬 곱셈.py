import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

ab = [[] for _ in range(n)]

for i in range(n):
    for j in range(k):
        ans = 0
        for l in range(m):
            ans += a[i][l] * b[l][j]
        
        ab[i].append(ans)

for i in range(n):
    print(*ab[i])
