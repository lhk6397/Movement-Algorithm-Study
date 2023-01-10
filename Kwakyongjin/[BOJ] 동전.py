import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    coins = list(map(int, input().split()))
    target = int(input().rstrip())
    d = [0 for _ in range(target+1)]
    d[0] = 1

    for coin in coins:
        for m in range(1, target+1):
            if m - coin >= 0:
                d[m] += d[m-coin]
    print(d[target])
