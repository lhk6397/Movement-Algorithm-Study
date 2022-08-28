# https://www.acmicpc.net/problem/11048
n, m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + graph[i-1][j-1]
print(dp[n][m])

'''
dx = [1, 0, 1]
dy = [0, 1, 1]
dp[0][0] = graph[0][0]
for i in range(n):
    for j in range(m):
        for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            candy = dp[i][j] + graph[nx][ny]
            if candy > dp[nx][ny]:
                dp[nx][ny] = candy
print(dp[n-1][m-1])
'''