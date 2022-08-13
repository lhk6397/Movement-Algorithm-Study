# https://www.acmicpc.net/problem/9461
dp = [1, 1, 1, 2, 2]
for i in range(5,101):
    dp.append(dp[i-5] + dp[i-1])
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n-1])