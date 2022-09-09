import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = int(input().rstrip())
table = list(list(map(int, input().split())) for _ in range(t))
table.sort(key=lambda x:x[1])
d = [0] * (n+1)
count = 0

for s, e, c in table:
    tmp = c
    for i in range(s,e):
        if d[i] + tmp >= m:
            tmp = m - d[i]
    for i in range(s,e):
        d[i] += tmp
    count += tmp

print(count)
