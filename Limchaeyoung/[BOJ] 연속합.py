n = int(input())
data = list(map(int, input().split()))
dp = [0] * len(data)
dp[0] = data[0]
for i in range(1, len(dp)):
    dp[i] = max(data[i], dp[i-1]+data[i])
print(max(dp))

# n = int(input())
# data = list(map(int, input().split()))
# dp = [-1000] * len(data)
# dp[0] = data[0]
# for i in range(1, len(dp)):
#     k = data[i-1] + data[i]
#     if k >= 0:
#         dp[i], data[i] = k, k
#     else:
#         dp[i], data[i] = data[i], 0
# print(max(dp))