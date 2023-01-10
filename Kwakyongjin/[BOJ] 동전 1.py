import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))
coins.sort()

d = [0 for _ in range(k+1)]
d[0] = 1

for coin in coins:
    for m in range(1, k+1):
        if m - coin >= 0:
            d[m] += d[m-coin]

print(d[k])
