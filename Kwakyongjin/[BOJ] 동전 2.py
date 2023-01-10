import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))

d = [0 for _ in range(k+1)]

for i in range(1, k+1):
    a = []
    for coin in coins:
        if coin <= i and d[i-coin] != -1:
            a.append(d[i-coin])
        
    if not a:
        d[i] = -1
    else:
        d[i] = min(a) + 1

print(d[k])
