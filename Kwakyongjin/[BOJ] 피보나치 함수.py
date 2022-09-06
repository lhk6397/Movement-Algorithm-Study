import sys
input = sys.stdin.readline

d = [0] * 41
d[0] = [1, 0]
d[1] = [0, 1]

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    for i in range(2, n+1):
        d[i] = [d[i-2][0] + d[i-1][0], d[i-2][1] + d[i-1][1]]

    print(d[n][0], d[n][1])
