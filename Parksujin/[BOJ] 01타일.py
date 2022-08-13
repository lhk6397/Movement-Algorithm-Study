# dp[i] = dp[i-1] + dp[i-2]
# 1과 00 타일 뿐이므로
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
  dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 반복문 내에서 나누기해야 메모리 초과 X
  
print(dp[n])