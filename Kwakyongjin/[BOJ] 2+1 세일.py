import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
price = [int(input().rstrip()) for _ in range(n)]
price.sort(reverse=True)
ans = 0
price = deque(price)

for i in range(n//3):
    item1, item2, item3 = price.popleft(), price.popleft(), price.popleft()

    ans += item1 + item2

for i in range(len(price)):
    ans += price.popleft()

print(ans)
