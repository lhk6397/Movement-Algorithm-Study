import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.insert(0, 0)
d = [0] * 100001
d[1] = lst[1]

for i in range(2, n+1):
    d[i] = d[i-1] + lst[i]

for i in range(m):
    a, b = map(int, input().split())
    print(d[b] - d[a-1])
