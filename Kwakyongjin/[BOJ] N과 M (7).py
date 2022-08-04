import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
result = []

def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in lst:
        result.append(i)
        dfs()
        result.pop()

dfs()
