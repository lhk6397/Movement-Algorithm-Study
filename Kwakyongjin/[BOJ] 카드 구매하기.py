import sys
input = sys.stdin.readline

n = int(input().rstrip())
p = list(map(int, input().split()))
p.insert(0,0)
d = [0 for _ in range(n+1)]
d[1] = p[1]
for i in range(2, n+1):
    _max = p[i]
    for j in range(1, i):
        _max = max(_max, d[j] + p[i-j])
    
    d[i] = _max

print(d[n])
