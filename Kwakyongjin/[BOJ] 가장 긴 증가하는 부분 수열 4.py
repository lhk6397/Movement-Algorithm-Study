import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))
d = [0 for _ in range(n)]
d[0] = 1
table = [[] for _ in range(n)]
table[0] = [a[0]]

for i in range(1, n):
    s = []
    t = []
    for j in range(i):
        if a[i] > a[j]:
            s.append(d[j])
            t.append(table[j])
    
    if not s:
        d[i] = 1
        table[i] = [a[i]]
    else:
        d[i] = max(s) + 1
        table[i] = t[s.index(max(s))] + [a[i]]

print(max(d))
print(*table[d.index(max(d))])
