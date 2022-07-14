'''
import itertools
n, m = map(int, input().split())
list = [x for x in range(1, n+1)]
sequence = itertools.permutations(list, m)
for x in sequence:
    for y in range(m):
        print(x[y], end=' ')
    print('')
'''
# 백트래킹
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for x in range(1, n+1):
        if visited[x]:
            continue
        visited[x] = True
        s.append(x)
        dfs()
        s.pop()
        visited[x] = False
n, m = map(int, input().split())
s = []
visited = [False] * (n+1)
dfs()