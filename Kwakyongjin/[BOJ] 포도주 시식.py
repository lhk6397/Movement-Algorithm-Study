import sys
input = sys.stdin.readline

n = int(input())
graph = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n == 1:
    dp[1] = graph[1]
else:
    dp[1] = graph[1]
    dp[2] = graph[1] + graph[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + graph[i], dp[i-3] + graph[i-1] + graph[i], dp[i-1])
print(max(dp))
