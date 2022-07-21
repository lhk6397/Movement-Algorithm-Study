n, target = map(int, input().split())
d = [-1] * (target + 1)
coins = []
for _ in range(n):
  coins.append(int(input()))
  
d[0] = 0

for i in range(1, target + 1):
  for coin in coins:
    if i % coin == 0:
      if d[i] > 0:
        d[i] = min(d[i], d[i-coin] + 1)
      else:
        d[i] = d[i-coin] + 1
print(d[target])

# 나동빈 코드

# d = [10001] * (m + 1) # 10001은 INF 값임(만들 수 없는 무한대 값)
# d[0] = 0
# for i in range(n):
#   for j in range(coins[i], target + 1)
#     if d[j - coins[i]] != 10001: # (i - k)원을 만드는 방법이 존재하면
#       d[j] = min(d[j], d[j - coins[i]] + 1)
# if d[target] == 10001:
#   print(-1)
# else:
#   print(d[m])