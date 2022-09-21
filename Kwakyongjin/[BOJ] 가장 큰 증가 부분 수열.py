import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))
d = [0 for _ in range(n)]
d[0] = a[0]

for i in range(1, n):
    s = []
    for j in range(i):
        if a[i] > a[j]:
            s.append(d[j])
    
    if not s:
        d[i] = a[i]
    else:
        d[i] = a[i] + max(s)

print(max(d))
