import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    graph = [list(map(int, input().rstrip().split())) for _ in range(2)]
    d = [[0]*n for _ in range(2)]
    if n == 1:
        d[0][0], d[1][0] = graph[0][0], graph[1][0]
        
    else:
        d[0][0], d[0][1], d[1][0], d[1][1] = graph[0][0], graph[1][0] + graph[0][1], graph[1][0], graph[0][0] + graph[1][1]
        
    for i in range(2, n):
        d[0][i] = max(d[1][i-2], d[1][i-1]) + graph[0][i]
        d[1][i] = max(d[0][i-2], d[0][i-1]) + graph[1][i]
    
    res = max(d[0][n-1], d[1][n-1])
    print(res)
