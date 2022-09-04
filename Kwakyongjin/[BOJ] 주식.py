import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    table = list(map(int, input().split()))
    profit = 0
    high_price = 0
    for i in range(n-1, -1, -1):
        if(table[i] > high_price):
            high_price = table[i]
        else:
            profit += high_price - table[i]    
    print(profit)

