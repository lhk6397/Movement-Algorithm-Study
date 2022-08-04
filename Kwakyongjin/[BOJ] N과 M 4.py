import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
start = 1

def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n+1):
        result.append(i)
        dfs(i)
        result.pop()

dfs(start)
