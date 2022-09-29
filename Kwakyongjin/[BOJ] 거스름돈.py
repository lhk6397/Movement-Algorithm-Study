import sys
input = sys.stdin.readline

n = int(input().rstrip())
money = [0 for _ in range(100001)]
money[1] = -1
money[2] = 1
money[3] = -1
money[4] = 2
money[5] = 1

for i in range(6, n+1):
    if money[i - 2] == -1 and money[i - 5] == -1:
        money[i] = -1

    elif money[i - 2] == -1:
        money[i] = money[i - 5] + 1

    elif money[i - 5] == -1:
        money[i] = money[i - 2] + 1

    else:
        money[i] = min(money[i-2], money[i-5]) + 1

print(money[n]) 
