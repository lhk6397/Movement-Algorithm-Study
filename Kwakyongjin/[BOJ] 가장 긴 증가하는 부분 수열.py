import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))
d = [0 for _ in range(n)]
d[0] = 1

for i in range(1, n):
    s = []
    for j in range(i):
        if a[i] > a[j]:
            s.append(d[j])
    
    if not s:
        d[i] = 1
    else:
        d[i] = max(s) + 1

print(max(d))
