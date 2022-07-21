import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = []
for _ in range(n):
    s = 0
    k = list(map(int, input().split()))
    for i in range(n):
        s += k[i]
        k[i] = s
    data.append(k)

for _ in range(m):
    sum = 0
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    for x in range(x1, x2+1):
        if y1 == 0:
            sum += data[x][y2]
        else:
            sum += data[x][y2] - data[x][y1-1]
    print(sum)

