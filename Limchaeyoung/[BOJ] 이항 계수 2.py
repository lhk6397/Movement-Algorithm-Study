n, k = map(int, input().split())
dp = [[1], [1, 1]]
for i in range(2, n+1):
    com = []
    com.append(1)
    for j in range(1, len(dp)):
        com.append(dp[i-1][j-1]+dp[i-1][j])
    com.append(1)
    dp.append(com)
print(dp[n][k]%10007)