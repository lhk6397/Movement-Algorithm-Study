import sys
input = sys.stdin.readline

n, q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] += A[i-1]+dp[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    
    print(dp[r]-dp[l-1])
