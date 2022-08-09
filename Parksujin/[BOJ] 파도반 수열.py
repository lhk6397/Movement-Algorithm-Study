# dp[i] = dp[i-3] + dp[i-2]

dp = [1, 1, 1, 2]
for j in range(4, 101):
  dp.append(dp[j-3] + dp[j-2])
  
T = int(input())
for i in range(T):
  N = int(input())
  print(dp[N-1])
  