import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(m):
    if b[i] in a:
        a.remove(b[i])
    
a = sorted(list(a))
print(len(a))
print(*a)
