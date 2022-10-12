import sys
input = sys.stdin.readline

g = int(input().rstrip())
p = int(input().rstrip())
parent = [i for i in range(g+1)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

gis = [int(input().rstrip()) for _ in range(p)]

cnt = 0 
for gi in gis:
    p = find(gi)
    if p == 0:
        break
    
    cnt += 1
    union(p-1, p)

print(cnt)
