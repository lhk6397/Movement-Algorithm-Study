import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    
    for j in range(k+1):
        if w <= j:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)
        else:
            d[i][j] = d[i-1][j]
    
print(d[n][k])
