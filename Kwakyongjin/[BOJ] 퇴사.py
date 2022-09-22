import sys
input = sys.stdin.readline

n = int(input().rstrip())
t = []
p = []
d = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    d.append(b)
d.append(0)
for i in range(n-1, -1, -1):
    if t[i] + i > n:
        d[i] = d[i + 1]
    else:
        d[i] = max(d[i + 1], p[i] + d[i+t[i]])
    
print(d[0])
