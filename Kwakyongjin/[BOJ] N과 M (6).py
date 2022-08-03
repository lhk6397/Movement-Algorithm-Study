import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
result = []
start = 0

def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, len(lst)):
        if not lst[i] in result:
            result.append(lst[i])
            dfs(i+1)
            result.pop()

dfs(start)
